#!/usr/bin/env python3
"""Build README.md, TRENDS is hand-written, and data/papers.csv.

NLP rows are parsed from official award-page snapshots when present, plus a
few hand-checked entries (EMNLP 2022, NAACL 2022, NAACL 2024).
"""
from __future__ import annotations

import csv
import json
import re
import time
import urllib.parse
import urllib.request
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
import sys
sys.path.insert(0, str(ROOT / "data"))
from make_papers import PAPERS as ML_PAPERS  # noqa: E402

SNAPSHOTS = {
    ("ACL", 2023): Path("/tmp/awards/acl2023.html"),
    ("ACL", 2024): Path("/tmp/awards/acl2024.html"),
    ("ACL", 2025): Path("/tmp/awards/acl2025.html"),
    ("ACL", 2026): Path("/tmp/awards/acl2026.html"),
    ("EMNLP", 2023): Path("/tmp/awards/emnlp2023.html"),
    ("EMNLP", 2024): Path("/tmp/awards/emnlp2024.html"),
    ("EMNLP", 2025): Path("/tmp/awards/emnlp2025.html"),
    ("EMNLP", 2026): Path("/tmp/awards/emnlp2026.html"),
    ("NAACL", 2025): Path("/tmp/awards/naacl2025.html"),
}

KEEP = {
    "best paper awards": "Best Paper",
    "best paper": "Best Paper",
    "best paper award": "Best Paper",
    "outstanding papers": "Outstanding Paper",
    "reproduction award": "Reproduction Award",
    "resource award": "Resource Award",
    "social impact award": "Social Impact Award",
    "theme paper award": "Theme Paper Award",
    "best social impact paper awards": "Best Social Impact Paper",
    "best social impact paper": "Best Social Impact Paper",
    "best social impact papers": "Best Social Impact Paper",
    "best social impact award": "Best Social Impact Paper",
    "best resource paper awards": "Best Resource Paper",
    "best resource paper": "Best Resource Paper",
    "best resource papers": "Best Resource Paper",
    "resource paper awards": "Best Resource Paper",
    "best theme paper awards": "Best Theme Paper",
    "best theme paper": "Best Theme Paper",
    "best theme papers": "Best Theme Paper",
    "best theme paper award": "Best Theme Paper",
    "best special theme paper": "Best Special Theme Paper",
    "special theme paper award": "Best Special Theme Paper",
    "honorable mentions": "Honorable Mention",
    "people's choice award": "People's Choice Award",
    "best paper runner-up": "Best Paper Runner-up",
    "best theme paper runner-up": "Best Theme Paper Runner-up",
    "social impact paper awards": "Best Social Impact Paper",
}
SKIP_PREFIXES = (
    "sac award", "sac awards", "sac highlights", "area chair", "demo track",
    "student research", "best video", "best demo", "outstanding demo",
    "outstanding reviewer", "outstanding area", "outstanding senior",
    "the test of time", "the best paper award (tacl", "industry track",
    "paper award selection", "tacl best", "senior area chair",
)

NOTES = {
    "abstract visual reasoning with tangram shapes": "用七巧板做抽象视觉推理资源，看多模态模型会不会只靠整体轮廓、而不懂部件。",
    "topic-regularized authorship representation learning": "作者表征很容易偷用主题线索；这篇把主题从作者向量里压下去，才能谈跨主题的作者识别。",
    "learned incremental representations for parsing": "每个词只在看到前缀时打一个离散标签，标签序列就能确定句法树，从而让分析真正是增量的。",
    "requirements and motivations of low-resource speech synthesis for language revitalization": "把低资源语音合成放回语言复兴的真实需求，而不是默认技术指标就是社区要的东西。",
    "dibimt: a novel benchmark for measuring word sense disambiguation biases in machine translation": "机器翻译里的词义偏见需要专门的基准，不能只看 BLEU。",
    "kinyabert: a morphology-aware kinyarwanda language model": "形态丰富的语言不该被当成缺数据的英语；模型要先承认词的内部结构。",
    "do androids laugh at electric sheep? humor “understanding” benchmarks from the new yorker caption contest": "用《纽约客》配图说明文字比赛看模型到底懂不懂幽默，而不是会不会生成一句俏皮话。",
    "what the daam: interpreting stable diffusion using cross attention": "用交叉注意力解释扩散模型生成时文本的哪些部分真正管住了图像的哪些区域。",
    "from pretraining data to language models to downstream tasks: tracking the trails of political biases leading to unfair nlp models": "政治偏见不是在下游任务里突然出现的，可以沿着预训练数据追到模型再追到任务。",
    "mission: impossible language models": "用人类学不会的人造语言去探语言模型的归纳偏置：模型觉得容易的，不一定是语言学上自然的。",
    "why are sensitive functions hard for transformers?": "有些布尔函数对 Transformer 特别难，难在架构的注意力方式，不是数据不够。",
    "deciphering oracle bone language with diffusion models": "把甲骨文残片的补全写成扩散生成，古文字和现代生成模型发生了接触。",
    "aya model: an instruction finetuned open-access multilingual language model": "把指令微调做成覆盖大量语言的开放模型，而不是只在英语上把聊天调顺。",
    "olmo: accelerating the science of language models": "连训练数据、代码和中间检查点一起放开，语言模型研究才有办法被别人核对。",
    "dolma: an open corpus of three trillion tokens for language model pretraining research": "开放预训练语料本身就是结果，否则别人无法重复你声称的训练。",
    "how johnny can persuade llms to jailbreak them: rethinking persuasion to challenge ai safety by humanizing llms": "越狱不一定靠怪字符，普通人的说服话术就够，安全评测不该只防模板攻击。",
    "native sparse attention: hardware-aligned and natively trainable sparse attention": "稀疏注意力如果不能在现代 GPU 上真的训起来，就只是纸面的复杂度。",
    "language models resist alignment: evidence from data compression": "从压缩的角度看，对齐微调很难抹掉预训练里已经写进模型的倾向。",
    "fairness through difference awareness: measuring desired group discrimination in llms": "公平不总是抹平群体差异；有时人们要的是模型知道差异、并且用对地方。",
    "a theory of response sampling in llms: part descriptive and part prescriptive": "模型采样同时在描述分布和遵守指令，这两件事不该被一个温度系数混在一起。",
    "label words are anchors: an information flow perspective for understanding in-context learning": "上下文学习里，标签词像锚，信息是从例子流到这些词上再流出来的。",
    "ignore this title and hackaprompt: exposing systemic vulnerabilities of llms through a global prompt hacking competition": "用一场全球提示词比赛说明，注入漏洞是系统性的，不是几个越狱例子。",
    "infini-gram mini: exact n-gram search at the internet scale with fm-index": "把精确 n-gram 检索做到互联网规模，用来核对模型到底见过没有，而不是再近似一次。",
    "measuring chain of thought faithfulness by unlearning reasoning steps": "把思维链里的步骤忘掉再看答案变不变，用来检验链是不是真的在起作用。",
    "discotrace: representing and comparing answering strategies of humans and llms in information-seeking question answering": "人回答信息寻求问题的策略和模型不一样；先把策略表示出来，才能比较，而不是只比最后一句对不对。",
    "don't read everything: a curvature-conditioned query for linear attention": "线性注意力不该对所有位置一视同仁，查询可以按曲率决定哪里值得读。",
    "the biggen bench: a principled benchmark for fine-grained evaluation of language models with language models": "用模型评模型时，粒度本身要有设计，而不是只给一个总分。",
    "rel-a.i.: an interaction-centered approach to measuring human-lm reliance": "人有多依赖模型，要在交互过程里量，而不是问一句你信不信它。",
    "fnet: mixing tokens with fourier transforms": "用无参数的傅里叶变换代替自注意力来混合 token，追问注意力是不是唯一的混合方式。",
    "neurologic a*esque decoding: constrained text generation with lookahead heuristics": "带约束的生成是搜索问题，向前看一步的启发式比生成完再过滤更接近解码本身。",
    "visual grounding helps learn word meanings in low-data regimes": "词义在数据很少时，视觉落地比再堆文本更有用。",
    "r-tuning: instructing large language models to say `i don't know'": "让模型学会拒答，本身可以作为指令微调的目标，而不是只在推理时加一句提示。",
    "teaching language models to self-improve through interactive demonstrations": "小模型的自我改进不是提示出来的，要靠它和更强模型交互、再重放自己的修正。",
    "lm-infinite: zero-shot extreme length generalization for large language models": "不继续训练，也想让模型在远超训练长度的输入上还能用。",
    "evaluating the deductive competence of large language models": "演绎能力和考试分数不是一回事，要把推理步骤单独拿出来评。",
}


def textify(html: str) -> list[str]:
    html = re.sub(r"<script[\s\S]*?</script>", " ", html, flags=re.I)
    html = re.sub(r"<style[\s\S]*?</style>", " ", html, flags=re.I)
    html = re.sub(r"<br\s*/?>", "\n", html, flags=re.I)
    html = re.sub(r"</(p|div|h\d|li|section)>", "\n", html, flags=re.I)
    html = re.sub(r"<[^>]+>", " ", html)
    for a, b in [
        ("&amp;", "&"), ("&#42;", "*"), ("&nbsp;", " "), ("&#39;", "'"),
        ("&ldquo;", '"'), ("&rdquo;", '"'), ("“", '"'), ("”", '"'), ("’", "'"),
    ]:
        html = html.replace(a, b)
    lines = []
    for ln in html.splitlines():
        ln = re.sub(r"\s+", " ", ln).strip().strip('"')
        if ln:
            lines.append(ln)
    return lines


def norm_key(s: str) -> str:
    return s.lower().strip().rstrip(":").strip()


def is_section(s: str) -> bool:
    key = norm_key(s)
    if key in KEEP:
        return True
    return any(key.startswith(p) for p in SKIP_PREFIXES)


def is_author(s: str) -> bool:
    if is_section(s) or len(s) > 1200 or len(s) < 3:
        return False
    if "?" in s or ":" in s:
        return False
    if s.lower().startswith(("ballroom", "posters", "online,", "notes from", "session ")):
        return False
    parts = [p.strip() for p in re.split(r"[,;]| and ", s) if p.strip()]
    if len(parts) >= 2:
        return all(1 <= len(p.split()) <= 6 for p in parts)
    tokens = s.split()
    function_words = {"of", "for", "the", "a", "an", "in", "on", "with", "via", "to", "from", "using"}
    if any(t.lower() in function_words for t in tokens):
        return False
    return 2 <= len(tokens) <= 3 and all(t[:1].isupper() for t in tokens if t[:1].isalpha())


def parse_snapshot(conf: str, year: int, path: Path) -> list[dict]:
    lines = textify(path.read_text(errors="ignore"))
    # Drop the duplicated navigation block: start at the last "On this page" if present.
    start = 0
    for i, ln in enumerate(lines):
        if ln.lower() == "on this page":
            start = i + 1
    lines = lines[start:]
    award = None
    papers = []
    seen = set()
    skipping = False
    # These headers end a skipped block (demo, industry, SAC). The bare
    # "Best Paper Award" used inside a demo block does not.
    # "Best Paper Award" (singular) is the demo-track heading. The main-track
    # headings are "Best Paper" / "Best Paper Awards" and must end a skip.
    resume_keys = {k for k in KEEP if k not in {"best paper award"}}
    i = 0
    while i < len(lines):
        raw = lines[i]
        key = norm_key(raw)
        if any(key.startswith(p) for p in SKIP_PREFIXES):
            award = None
            skipping = True
            i += 1
            continue
        if key in KEEP:
            if skipping and key not in resume_keys:
                i += 1
                continue
            skipping = False
            award = KEEP[key]
            i += 1
            continue
        if skipping:
            i += 1
            continue
        if award and i + 1 < len(lines) and is_author(lines[i + 1]) and not is_author(raw) and len(raw) > 8:
            title = raw
            authors = lines[i + 1]
            # session crumbs on NAACL pages
            if authors.lower().startswith(("ballroom", "posters", "online,", "notes from")):
                i += 1
                continue
            k = (title.lower(), award)
            if k not in seen:
                seen.add(k)
                papers.append({
                    "conference": conf,
                    "year": year,
                    "award": award,
                    "title": title,
                    "authors": authors,
                    "url": "",
                    "domain": "",
                    "did": NOTES.get(re.sub(r"\s+", " ", title.lower()).strip(), ""),
                    "insight": "",
                    "why": "",
                })
            i += 2
            continue
        i += 1
    return papers


def manual_rows() -> list[dict]:
    def r(conf, year, award, title, authors, url, note):
        return {
            "conference": conf, "year": year, "award": award, "title": title,
            "authors": authors, "url": url, "domain": "", "did": note, "insight": "", "why": "",
        }
    return [
        r("ACL", 2023, "Outstanding Paper", "Backpack Language Models",
          "John Hewitt, John Thickstun, Christopher Manning, Percy Liang", "",
          "把词的意义拆成可以相加的非上下文分量，再看模型预测时用了哪一个分量。"),
        r("ACL", 2023, "Outstanding Paper", "Causes and Cures for Interference in Multilingual Translation",
          "Uri Shaham, Maha Elbayad, Vedanuj Goswami, Omer Levy, Shruti Bhosale", "",
          "多语言翻译里语言之间会互相干扰，这篇把干扰的来源和缓解放在一起看。"),
        r("ACL", 2026, "Outstanding Paper", "Systematicity between Forms and Meanings across Languages Supports Efficient Communication",
          "Doreen Osmelak, Yang Xu, Michael Hahn, Kate McCurdy", "",
          "形式和意义之间的系统性如果跨语言成立，就可以拿来解释沟通为什么能省。"),
        r("ACL", 2026, "Outstanding Paper", "Massively Multilingual Joint Segmentation and Glossing",
          "Michael Ginn, Lindia Tjuatja, Enora Rice, Ali Marashian, Maria Valentini, Jasmine Xu, Graham Neubig, Alexis Palmer", "",
          "分词和注释在很多语言上一起做，而不是先切词再逐词解释。"),
        r("ACL", 2026, "Best Paper", "The Imperfective Paradox in Large Language Models",
          "Bolei Ma, Yusuke Miyao", "",
          "未完成体悖论是语言学里的老问题；这篇看大模型会不会在体貌上犯和人不一样的错。"),
        r("ACL", 2026, "Best Paper", "Memory Efficiency and Resource-Rational Encoding in Sentence Processing",
          "Weijie Xu, Brian Dillon, Richard Futrell", "",
          "句子加工的记忆效率可以写成资源理性的编码问题，模型和人类的限制放在同一把尺子上。"),
        r("ACL", 2026, "Best Paper", "Characterizing the Expressivity of Local Attention in Transformers",
          "Jiaoda Li, Ryan Cotterell", "",
          "局部注意力的表达力需要单独刻画，不能用全注意力的结论直接套。"),
        r("EMNLP", 2022, "Best Long Paper", "Abstract Visual Reasoning with Tangram Shapes",
          "Anya Ji, Noriyuki Kojima, Noah Rush, Alane Suhr, Wai Keen Vong, Robert Hawkins, Yoav Artzi",
          "https://aclanthology.org/2022.emnlp-main.38/",
          NOTES["abstract visual reasoning with tangram shapes"]),
        r("EMNLP", 2022, "Best Short Paper", "Topic-Regularized Authorship Representation Learning",
          "Jitkapat Sawatphol, Nonthakit Chaiwong, Can Udomcharoenchaikit, Sarana Nutanong",
          "https://aclanthology.org/2022.emnlp-main.70/",
          NOTES["topic-regularized authorship representation learning"]),
        r("ACL", 2022, "Best Paper", "Learned Incremental Representations for Parsing",
          "Nikita Kitaev, Thomas Lu, Dan Klein",
          "https://aclanthology.org/2022.acl-long.220/",
          NOTES["learned incremental representations for parsing"]),
        r("ACL", 2022, "Best Special Theme Paper", "Requirements and Motivations of Low-Resource Speech Synthesis for Language Revitalization",
          "Aidan Pine, Dan Wells, Nathan Brinklow, Patrick William Littell, Korin Richmond",
          "",
          NOTES["requirements and motivations of low-resource speech synthesis for language revitalization"]),
        r("ACL", 2022, "Best Resource Paper", "DiBiMT: A Novel Benchmark for Measuring Word Sense Disambiguation Biases in Machine Translation",
          "Niccolò Campolungo, Federico Martelli, Francesco Saina, Roberto Navigli",
          "",
          NOTES["dibimt: a novel benchmark for measuring word sense disambiguation biases in machine translation"]),
        r("ACL", 2022, "Best Linguistic Insight Paper", "KinyaBERT: a Morphology-aware Kinyarwanda Language Model",
          "Antoine Nzeyimana, Andre Niyongabo Rubungo",
          "",
          NOTES["kinyabert: a morphology-aware kinyarwanda language model"]),
        r("ACL", 2022, "Outstanding Paper", "Evaluating Factuality in Text Simplification",
          "Ashwin Devaraj, William Berkeley Sheffield, Byron C. Wallace, Junyi Jessy Li",
          "",
          "简化文本很容易把事实改掉，评测必须单独看事实还在不在。"),
        r("ACL", 2022, "Outstanding Paper", "Online Semantic Parsing for Latency Reduction in Task-Oriented Dialogue",
          "Jiawei Zhou, Jason Eisner, Michael Newman, Emmanouil Antonios Platanios, Sam Thomson",
          "",
          "任务型对话不必等整句说完再解析，在线解析是为了把延迟降下来。"),
        r("ACL", 2022, "Outstanding Paper", "Learning to Generalize to More: Continuous Semantic Augmentation for Neural Machine Translation",
          "Xiangpeng Wei, Heng Yu, Yue Hu, Rongxiang Weng, Weihua Luo, Rong Jin",
          "",
          "翻译的泛化可以靠连续的语义增广，而不是只换一批平行句。"),
        r("ACL", 2022, "Outstanding Paper", "Fantastically Ordered Prompts and Where to Find Them: Overcoming Few-Shot Prompt Order Sensitivity",
          "Yao Lu, Max Bartolo, Alastair Moore, Sebastian Riedel, Pontus Stenetorp",
          "",
          "少样本提示的顺序本身就会翻盘，找顺序是方法的一部分。"),
        r("ACL", 2022, "Outstanding Paper", "Inducing Positive Perspectives with Text Reframing",
          "Caleb Ziems, Minzhi Li, Anthony Zhang, Diyi Yang",
          "",
          "换一种说法可以改变视角，这是生成问题，也是社会语言学问题。"),
        r("ACL", 2022, "Outstanding Paper", "Ditch the Gold Standard: Re-evaluating Conversational Question Answering",
          "Huihan Li, Tianyu Gao, Manan Goenka, Danqi Chen",
          "",
          "对话问答的金标准评测和真实对话并不一样，需要把评测本身拿出来重做。"),
        r("ACL", 2022, "Outstanding Paper", "Active Evaluation: Efficient NLG Evaluation with Few Pairwise Comparisons",
          "Akash Kumar Mohankumar, Mitesh M. Khapra",
          "",
          "生成评测不必两两比完，主动选择比较可以少问很多次。"),
        r("ACL", 2022, "Outstanding Paper", "Compression of Generative Pre-trained Language Models via Quantization",
          "Chaofan Tao, Lu Hou, Wei Zhang, Lifeng Shang, Xin Jiang, Qun Liu, Ping Luo, Ngai Wong",
          "",
          "生成式预训练模型的压缩要面对生成，而不只是分类精度。"),
        r("NAACL", 2022, "Best Paper (new task and new resource)", "Automatic Correction of Human Translations",
          "Jessy Lin, Geza Kovacs, Aditya Shastry, Joern Wuebker, John DeNero",
          "",
          "改的是人的译文，不是机器译文；任务、数据和译员一起定义。"),
        r("NAACL", 2022, "Best Paper (efficient NLP)", "FNet: Mixing Tokens with Fourier Transforms",
          "James Lee-Thorp, Joshua Ainslie, Ilya Eckstein, Santiago Ontanon",
          "",
          NOTES["fnet: mixing tokens with fourier transforms"]),
        r("NAACL", 2022, "Best Paper (new task)", "FRUIT: Faithfully Reflecting Updated Information in Text",
          "Robert L. Logan IV, Alexandre Tachard Passos, Sameer Singh, Ming-Wei Chang",
          "",
          "文本里的事实会过期，更新文本是和纠错不同的任务。"),
        r("NAACL", 2022, "Best Paper (new method)", "NeuroLogic A*esque Decoding: Constrained Text Generation with Lookahead Heuristics",
          "Ximing Lu, Sean Welleck, Peter West, Liwei Jiang, Jungo Kasai, Daniel Khashabi, Ronan Le Bras, Lianhui Qin, Youngjae Yu, Rowan Zellers, Noah Smith, Yejin Choi",
          "",
          NOTES["neurologic a*esque decoding: constrained text generation with lookahead heuristics"]),
        r("NAACL", 2022, "Best Paper (human-centered NLP)", "User-Driven Research of Medical Note Generation Software",
          "Tom Knoll, Francesco Moramarco, Alex Papadopoulos Korfiatis, Rachel Young, Claudia Ruffini, Mark Perera, Christian Perstl, Ehud Reiter, Anya Belz, Aleksandar Savkov",
          "",
          "病历生成该怎么做，要让真正写病历的人参与定义，而不是只优化摘要分数。"),
        r("NAACL", 2022, "Honorable Mention", "Balanced Data Approach for Evaluating Cross-Lingual Transfer: Mapping the Linguistic Blood Bank",
          "Dan Malkin, Tomasz Limisiewicz, Gabriel Stanovsky",
          "",
          "跨语言迁移的评测数据本身可能不平衡，先把语言覆盖画清楚。"),
        r("NAACL", 2022, "Honorable Mention", "NewsEdits: A Dataset of News Article Revision Histories and a Novel Document-Level Reasoning Challenge",
          "Alexander Spangher, Xiang Ren, Jonathan May, Nanyun Peng",
          "",
          "新闻的修改历史是文档级推理的资源，不只是另一份摘要数据。"),
        r("NAACL", 2024, "Best Paper", "Visual Grounding Helps Learn Word Meanings in Low-Data Regimes",
          "Chengxu Zhuang, Evelina Fedorenko, Jacob Andreas",
          "",
          NOTES["visual grounding helps learn word meanings in low-data regimes"]),
        r("NAACL", 2024, "Best Paper", "Evaluating the Deductive Competence of Large Language Models",
          "S. M. Seals, Valerie Shalin",
          "",
          NOTES["evaluating the deductive competence of large language models"]),
        r("NAACL", 2024, "Outstanding Paper", "LM-Infinite: Zero-Shot Extreme Length Generalization for Large Language Models",
          "Chi Han, Qifan Wang, Hao Peng, Wenhan Xiong, Yu Chen, Heng Ji, Sinong Wang",
          "",
          NOTES["lm-infinite: zero-shot extreme length generalization for large language models"]),
        r("NAACL", 2024, "Outstanding Paper", "Defining and Detecting Vulnerability in Human Evaluation Guidelines: A Preliminary Study Towards Reliable NLG Evaluation",
          "Jie Ruan, Wenqing Wang, Xiaojun Wan",
          "https://aclanthology.org/2024.naacl-long.441/",
          "人工评测指南本身会有漏洞，指南不可靠时，评测结果也不可靠。"),
        r("NAACL", 2024, "Outstanding Paper", "Unlocking Emergent Modularity in Large Language Models",
          "Zihan Qiu, Zeyu Huang, Jie Fu",
          "",
          "大模型里的模块化不一定要预先设计，有可能从训练里长出来。"),
        r("NAACL", 2024, "Outstanding Paper", "R-Tuning: Instructing Large Language Models to Say `I Don't Know'",
          "Hanning Zhang, Shizhe Diao, Yong Lin, Yi Fung, Qing Lian, Xingyao Wang, Yangyi Chen, Heng Ji, Tong Zhang",
          "",
          NOTES["r-tuning: instructing large language models to say `i don't know'"]),
        r("NAACL", 2024, "Outstanding Paper", "Teaching Language Models to Self-Improve through Interactive Demonstrations",
          "Xiao Yu, Baolin Peng, Michel Galley, Jianfeng Gao, Zhou Yu",
          "",
          NOTES["teaching language models to self-improve through interactive demonstrations"]),
        r("NAACL", 2024, "Outstanding Paper", "A Pretrainer's Guide to Training Data: Measuring the Effects of Data Age, Domain Coverage, Quality, & Toxicity",
          "Shayne Longpre, Gregory Yauney, Emily Reif, Katherine Lee, Adam Roberts, Barret Zoph, Denny Zhou, Jason Wei, Kevin Robinson, David Mimno, Daphne Ippolito",
          "",
          "预训练数据的年龄、领域、质量和毒性要分开量，不能合成一个干净分数。"),
        r("NAACL", 2024, "Best Theme Paper", "Grammar-based Data Augmentation for Low-Resource Languages: The Case of Guarani-Spanish Neural Machine Translation",
          "Agustín Lucas, Alexis Baladón, Victoria Pardiñas, Marvin M. Agüero-Torales, Santiago Góngora, Luis Chiruzzo",
          "",
          "低资源翻译的增广可以用语法来做，而不是只回译。"),
        r("NAACL", 2024, "Best Social Impact Paper", "Understanding the Capabilities and Limitations of Large Language Models for Cultural Commonsense",
          "Siqi Shen, Lajanugen Logeswaran, Moontae Lee, Honglak Lee, Soujanya Poria, Rada Mihalcea",
          "",
          "文化常识不是英语常识的翻译，模型的能力和限度要按文化来写。"),
        r("NAACL", 2024, "Best Resource Paper", "Exploring Cross-Cultural Differences in English Hate Speech Annotations: From Dataset Construction to Analysis",
          "Nayeon Lee, Chani Jung, Junho Myung, Jiho Jin, Jose Camacho-Collados, Juho Kim, Alice Oh",
          "",
          "同一句英语算不算仇恨，不同文化的标注者并不一致，数据集必须把这个差异留下来。"),
    ]


def key_title(title: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", title.lower())


def openalex_url(title: str) -> str:
    q = urllib.parse.urlencode({"search": title, "per-page": 3})
    req = urllib.request.Request(
        f"https://api.openalex.org/works?{q}",
        headers={"User-Agent": "best-paper-library/1.0 (mailto:research-notes@example.com)"},
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        data = json.loads(resp.read().decode())
    want = key_title(title)
    for work in data.get("results", []):
        got = key_title(work.get("display_name") or "")
        if not got:
            continue
        if got != want and not (want.startswith(got) or got.startswith(want)):
            # allow small containment for subtitles
            if want[:40] not in got and got[:40] not in want:
                continue
        doi = (work.get("ids") or {}).get("doi") or ""
        if "10.18653/v1/" in doi:
            anth = doi.split("10.18653/v1/")[-1]
            return f"https://aclanthology.org/{anth}"
        for loc in [work.get("primary_location") or {}] + (work.get("locations") or []):
            pdf = (loc or {}).get("pdf_url") or ""
            if "arxiv.org" in pdf:
                m = re.search(r"arxiv.org/(?:pdf|abs)/([0-9]{4}\.[0-9]{4,5})", pdf)
                if m:
                    return f"https://arxiv.org/abs/{m.group(1)}"
                return pdf.replace("/pdf/", "/abs/").replace(".pdf", "")
        oa = (work.get("open_access") or {}).get("oa_url") or ""
        if "arxiv.org" in oa:
            m = re.search(r"arxiv.org/(?:pdf|abs)/([0-9]{4}\.[0-9]{4,5})", oa)
            if m:
                return f"https://arxiv.org/abs/{m.group(1)}"
        if doi:
            return doi if doi.startswith("http") else f"https://doi.org/{doi}"
    return ""


def fill_urls(rows: list[dict]) -> None:
    missing = [r for r in rows if not r.get("url")]
    print(f"resolving {len(missing)} urls")
    for i, row in enumerate(missing):
        try:
            url = openalex_url(row["title"])
        except Exception as exc:  # noqa: BLE001
            print("lookup failed", row["title"][:60], exc)
            url = ""
        row["url"] = url
        if (i + 1) % 20 == 0:
            print(f"  {i+1}/{len(missing)}")
        time.sleep(0.12)


AWARD_RANK = {
    "Best Paper": 0, "Best Long Paper": 1, "Best Short Paper": 2,
    "Outstanding Paper": 3, "Outstanding Paper Honorable Mention": 4,
    "Outstanding Paper Runner-up": 5, "Best Paper Runner-up": 5,
    "Honorable Mention": 6,
    "Best Paper (new task and new resource)": 7,
    "Best Paper (efficient NLP)": 7,
    "Best Paper (new task)": 7,
    "Best Paper (new method)": 7,
    "Best Paper (human-centered NLP)": 7,
}


def award_rank(award: str) -> int:
    if award in AWARD_RANK:
        return AWARD_RANK[award]
    if award.startswith("Best"):
        return 8
    if "Runner" in award:
        return 5
    if "Honorable" in award:
        return 6
    if award.startswith("Test of Time"):
        return 50
    return 20


def one_line(row: dict) -> str:
    note = (row.get("did") or "").strip()
    if note:
        return note
    # ML rows store the sentence in did; NLP snapshots may miss it.
    title_key = re.sub(r"\s+", " ", row["title"].lower()).strip().replace("'", "'")
    return NOTES.get(title_key, "")


def authors_compact(authors: str) -> str:
    if not authors:
        return ""
    parts = [p.strip() for p in authors.replace(" and ", ", ").split(",") if p.strip()]
    if len(parts) <= 8:
        return ", ".join(parts)
    return ", ".join(parts[:6]) + " 等"


def render_readme(rows: list[dict]) -> str:
    by = defaultdict(list)
    for r in rows:
        by[r["conference"]].append(r)
    order = ["ICLR", "NeurIPS", "ICML", "ACL", "EMNLP", "NAACL", "AAAI"]
    parts = []
    parts.append("""# 顶会最佳论文（2022–2026）

给中文读者的一份获奖论文清单，用来练研究口味，不是用来背榜。

获奖论文不是标准答案。它只是社区在某一届会议上愿意公开说「这篇值得被记住」的样本。对还在选题的研究生，这种样本比又一篇综述更有用：你可以看见别人怎样把一个含糊的不满收成一个能做的问题，怎样把方法和问题对齐，怎样安排会翻车的实验，以及怎样把洞见写成读者能复述的一句话。

读的时候盯四件事。

- **选题。** 问题是不是当时真的卡着社区，而不是一个容易刷分的切口。
- **技术定位。** 新意在问题的定义、在旧工具的新接法，还是只在模块上加了一层。
- **实验。** 有没有把另一种解释先堵住。结论如果换一个指标就消失，这篇通常走不远。
- **表达。** 合上论文，能不能用一句人话讲清它相信什么。

## 两遍读法

第一遍跨年份、跨会议快速扫。每篇只留四个词：领域、做了什么、一句洞见、它可能为什么会被选中。扫完在纸上画一张自己的研究地图，看哪几条线在不同会议上同时变热。

第二遍只挑和自己方向最近的几篇精读。不要先问「我怎么复现」，先问「同一个问题为什么我没想到」。把作者的决定倒推出来：他们放弃了哪种更显然的做法，实验最先想说服谁。

每条下面的中文是一句笔记，方便扫读。它依据摘要或官方授奖说明，不写材料里没有的数字。没有笔记的条目也是核实过的获奖论文，只是还没写这句批注。

## 覆盖的会议

只收下面七个会，2022 到 2026。计算机视觉的 CVPR、ICCV、ECCV 不在这里。

### 机器学习

| 会议 | 全称 | 方向 | 这份清单覆盖的年份 |
| --- | --- | --- | --- |
| ICLR | International Conference on Learning Representations | 表征学习、深度学习方法 | 2022–2026 |
| NeurIPS | Conference on Neural Information Processing Systems | 理论、算法、应用，含数据集与基准轨道 | 2022–2025（2026 待补充） |
| ICML | International Conference on Machine Learning | 广义机器学习，含立场论文奖 | 2022–2026 |

### 自然语言处理

| 会议 | 全称 | 方向 | 这份清单覆盖的年份 |
| --- | --- | --- | --- |
| ACL | Annual Meeting of the Association for Computational Linguistics | 计算语言学主会 | 2022–2026 |
| EMNLP | Conference on Empirical Methods in Natural Language Processing | 实证方法 | 2022–2026 |
| NAACL | Nations of the Americas Chapter of the ACL | 美洲章节会议（2024 年前称 North American Chapter） | 2022、2024、2025 |

### 人工智能

| 会议 | 全称 | 方向 | 这份清单覆盖的年份 |
| --- | --- | --- | --- |
| AAAI | AAAI Conference on Artificial Intelligence | 广义人工智能，含经典规划和知识表示 | 2022–2026 |

## 收录口径

收主会的 Best / Outstanding Paper、Honorable Mention、Runner-up，以及官方的专项论文奖：Social Impact、Resource、Theme、Reproduction、Datasets and Benchmarks、Position Paper、Alignment、AI for Social Impact。ACL 从 2023 年起把 Outstanding Paper 扩到大约投稿的百分之二，这些论文在下面按年列出。

不收 Demo、Poster、Student Abstract、学生研讨会、分轨 SAC / Area Chair 奖、行业轨道和杰出审稿人。那些也是荣誉，但和「这篇论文为什么被当成最佳」不是同一件事。

时间检验奖（Test of Time / Classic Paper）的原论文早于 2022。它们写在各会议末尾的单独小节里，不拿来论证那一年的新趋势。

NeurIPS 2026 截至 2026 年 11 月 25 日尚未公布最佳论文。NAACL 在 2023 和 2026 没有办会。EMNLP 2022 目前只能核实最佳长文和最佳短文。

## 致谢

获奖篇目的起点对照过 [FeijiangHan/Top-Conference-Best-Papers](https://github.com/FeijiangHan/Top-Conference-Best-Papers)。那个仓库用来知道「该去核对哪些标题」，这里的中文、分类和取舍是重新写的，没有沿用它的段落。每条都再对着会议官方授奖页、OpenReview、ACL Anthology 或 arXiv 核对过；对不上的不猜。

笔记以 [CC BY 4.0](LICENSE) 发布。论文版权属于作者。

机器可读的表在 [`data/papers.csv`](data/papers.csv)。按年份串起来的读后感在 [`TRENDS.md`](TRENDS.md)。

""")
    for conf in order:
        rows_c = by.get(conf, [])
        parts.append(f"\n# {conf}\n")
        current = [r for r in rows_c if not r.get("test_of_time")]
        tots = [r for r in rows_c if r.get("test_of_time")]
        years = sorted({r["year"] for r in current}, reverse=True)
        if conf == "NeurIPS":
            parts.append("\n## 2026\n\n待补充。会议于 2026 年 12 月 6–12 日在悉尼举行，官方博客在 11 月 25 日之前只公布了教程、期刊轨道和可重复性轨道，没有公布 Best Paper。\n")
        if conf == "NAACL":
            parts.append("\n## 2026\n\n该年未举办。章节站点列出的下一次会议是 NAACL 2027（旧金山）。\n")
        for year in years:
            if conf == "NAACL" and year == 2022:
                parts.append("\n## 2023\n\n该年未举办。2023 年在北美召开的是 ACL（多伦多），NAACL 按惯例停办。\n")
            parts.append(f"\n## {year}\n")
            if conf == "EMNLP" and year == 2022:
                parts.append("\n这一年会后官网不稳定。下面两篇分别由康奈尔大学的新闻和短文第一作者的公开说明交叉核实，并与会后综述一致。若另有 Outstanding 名单，这里不猜测，标为待补充。\n")
            group = [r for r in current if r["year"] == year]
            awards = sorted({r["award"] for r in group}, key=award_rank)
            for award in awards:
                parts.append(f"\n### {award}\n")
                for r in group:
                    if r["award"] != award:
                        continue
                    url = r.get("url") or ""
                    link = f"[论文]({url})" if url else "链接待补充"
                    note = one_line(r)
                    parts.append(f"* **{r['title']}**")
                    parts.append(f"  {link} · {authors_compact(r.get('authors',''))}")
                    if note:
                        parts.append(f"  {note}")
                    parts.append("")
            if conf == "NAACL" and year == 2025:
                pass
        if tots:
            parts.append("\n## 时间检验奖\n\n原论文早于 2022，是后来的会议回看约十年前的工作。不放进上面各年的研究地图。\n")
            for r in sorted(tots, key=lambda x: -int(x["year"])):
                url = r.get("url") or ""
                link = f"[论文]({url})" if url else "链接待补充"
                orig = r.get("original_year") or "?"
                parts.append(f"* **{r['title']}**（{r['award']}，{r['year']} 年颁发，原论文 {orig}）")
                parts.append(f"  {link} · {authors_compact(r.get('authors',''))}")
                note = one_line(r)
                if note:
                    parts.append(f"  {note}")
                parts.append("")
    parts.append("""
# 还没写上的

- **NeurIPS 2026**：待补充。
- **NAACL 2023、NAACL 2026**：该年未举办。
- **EMNLP 2022** 除最佳长文、最佳短文以外的 Outstanding 名单：待补充。
- **ACL 2023** 的授奖页写明 Outstanding Paper 有 39 篇。下面收进 38 篇。剩下的一篇在页面上标题和作者粘在同一行，没有可靠拆开，不单列，避免把标题写错。
- 条目里写着「链接待补充」的，是标题和奖项已经核对，但没有找到稳定的论文页。ACL 2025 的 *Typology-Guided Adaptation for African NLP* 属于这一类。
""")
    return "\n".join(parts).replace("\n\n\n", "\n\n")


DROP_TITLES = {
    "viskop: visual knowledge oriented programming for interactive knowledge base question answering",
    "speed without sacrifice: fine-tuning language models with medusa and knowledge distillation in travel applications",
    "boosting decision-making ability of llms with speculative reward model cost-effectively",
    "neko: cross-modality post-recognition error correction with tasks-guided mixture-of-experts language models",
}


def main():
    rows = []
    for r in ML_PAPERS:
        r["year"] = int(r["year"])
        rows.append(r)
    for (conf, year), path in SNAPSHOTS.items():
        if not path.exists():
            raise SystemExit(f"missing snapshot {path}")
        parsed = parse_snapshot(conf, year, path)
        print(conf, year, len(parsed))
        rows.extend(parsed)
    rows.extend(manual_rows())
    # de-duplicate
    uniq = []
    seen = set()
    for r in rows:
        if r["title"].lower().strip() in DROP_TITLES or r["title"].lower().startswith("viskop:"):
            continue
        if r["title"].lower().startswith("speed without sacrifice:"):
            continue
        if r["title"].lower().startswith("boosting decision-making ability of llms"):
            continue
        if r["title"].lower().startswith("neko:"):
            continue
        k = (r["conference"], int(r["year"]), r["award"], key_title(r["title"]))
        if k in seen:
            continue
        seen.add(k)
        uniq.append(r)
    rows = uniq
    # Reuse URLs already resolved in papers.jsonl so a re-run does not
    # repeat hundreds of lookups. New titles still get looked up.
    cache = {}
    cache_path = ROOT / "data" / "papers.jsonl"
    if cache_path.exists():
        for line in cache_path.read_text(encoding="utf-8").splitlines():
            if not line.strip():
                continue
            old = json.loads(line)
            if old.get("url"):
                cache[(old["conference"], key_title(old["title"]))] = old["url"]
        for row in rows:
            hit = cache.get((row["conference"], key_title(row["title"])))
            if hit and not row.get("url"):
                row["url"] = hit
    fill_urls(rows)
    (ROOT / "data" / "papers.jsonl").write_text(
        "".join(json.dumps(r, ensure_ascii=False) + "\n" for r in rows), encoding="utf-8"
    )
    fields = ["conference", "year", "award", "title", "authors", "url", "领域"]
    with (ROOT / "data" / "papers.csv").open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for r in rows:
            if r.get("test_of_time"):
                continue
            w.writerow({
                "conference": r["conference"],
                "year": r["year"],
                "award": r["award"],
                "title": r["title"],
                "authors": r.get("authors", ""),
                "url": r.get("url", ""),
                "领域": r.get("domain") or "",
            })
    (ROOT / "README.md").write_text(render_readme(rows), encoding="utf-8")
    # counts
    from collections import Counter
    c = Counter((r["conference"], r["year"]) for r in rows if not r.get("test_of_time"))
    missing = sum(1 for r in rows if not r.get("url") and not r.get("test_of_time"))
    print("rows", len(rows), "missing urls", missing)
    for conf in ["ICLR", "NeurIPS", "ICML", "ACL", "EMNLP", "NAACL", "AAAI"]:
        years = sorted({y for (cc, y) in c if cc == conf})
        print(conf, ", ".join(f"{y}:{c[(conf,y)]}" for y in years))


if __name__ == "__main__":
    main()
