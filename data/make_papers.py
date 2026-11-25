#!/usr/bin/env python3
"""Hand-written records. Run to emit data/papers.jsonl."""
import json
from pathlib import Path

OUT = Path(__file__).with_name("papers.jsonl")

def P(conference, year, award, title, authors, url, domain, did, insight, why, tot=False, original_year=None):
    row = {
        "conference": conference,
        "year": year,
        "award": award,
        "title": title,
        "authors": authors,
        "url": url,
        "domain": domain,
        "did": did,
        "insight": insight,
        "why": why,
    }
    if tot:
        row["test_of_time"] = True
        row["original_year"] = original_year
    return row

PAPERS = []

def add(*rows):
    PAPERS.extend(rows)

# ---------------------------------------------------------------------------
# ICLR
# ---------------------------------------------------------------------------
add(
P("ICLR","2022","Outstanding Paper","Analytic-DPM: an Analytic Estimate of the Optimal Reverse Variance in Diffusion Probabilistic Models","Fan Bao, Chongxuan Li, Jun Zhu, Bo Zhang","https://openreview.net/forum?id=0xiJLKH-ufZ","扩散模型","给出扩散模型最优反向方差和对应 KL 的解析形式，并用预训练 score 做免训练估计。","反向过程里最贵的那一项方差，其实不必再训一个网络去拟合。","它把一个被当成工程调参的量写成可计算的闭式，理论和可插拔的推理改进绑在一起。"),
P("ICLR","2022","Outstanding Paper","Hyperparameter Tuning with Renyi Differential Privacy","Nicolas Papernot, Thomas Steinke","https://openreview.net/forum?id=-70L8lpp9DF","差分隐私","指出反复调超参会把隐私账本算漏，并在 Rényi 差分隐私里给搜索过程补上保证。","隐私证明通常假设算法只跑一次，真实流程却在同一批数据上试了很多组超参。","它打中的是差分隐私落地时人人都在犯、论文里却很少入账的一步。"),
P("ICLR","2022","Outstanding Paper","Learning Strides in Convolutional Neural Networks","Rachid Riad, Olivier Teboul, David Grangier, Neil Zeghidour","https://openreview.net/forum?id=M752z9FKJP","卷积网络","提出 DiffStride，在傅里叶域里学习下采样窗口，让步长变成可训练的。","卷积步长长期靠手调，是因为下采样本身不可微，不是因为最优步长不存在。","问题人人遇到，解法又小又干净，评委会把它当成会进工具箱的那种论文。"),
P("ICLR","2022","Outstanding Paper","Expressiveness and Approximation Properties of Graph Neural Networks","Floris Geerts, Juan L. Reutter","https://openreview.net/forum?id=wIzUeM3TAU","图神经网络","用张量语言重写 GNN 的表达力问题，把分离能力接到 Weisfeiler-Leman 和树宽上。","比较两种 GNN 谁更强，可以先比它们的张量计算，而不必每次重证一遍 WL。","它给架构设计者一个不用先成为逻辑学家也能用的表达力工具。"),
P("ICLR","2022","Outstanding Paper","Comparing Distributions by Measuring Differences that Affect Decision Making","Shengjia Zhao, Abhishek Sinha, Yutong He, Aidan Perreault, Jiaming Song, Stefano Ermon","https://openreview.net/forum?id=KB5onONJIAU","分布比较","定义一类由决策损失诱导的差异，用来比较两个分布在具体决策上差多少。","JS 散度和 MMD 不告诉你差异会不会改变决定；把决策任务写进差异里，比较就有了用途。","方法能覆盖已有散度，又允许使用者直接声明自己在乎哪种损失。"),
P("ICLR","2022","Outstanding Paper","Neural Collapse Under MSE Loss: Proximity to and Dynamics on the Central Path","X.Y. Han, Vardan Papyan, David L. Donoho","https://openreview.net/forum?id=w1UbdvWH_R3","训练动力学","在均方误差下拆开神经坍缩，并沿一条中心路径写出可预测的动力学。","交叉熵难分析时，换到 MSE 仍能看到分类器贴着类均值走的那条路径。","它把一个到处出现的经验现象写成可以往下算的动力学，而不是再描述一遍现象。"),
P("ICLR","2022","Outstanding Paper","Bootstrapped Meta-Learning","Sebastian Flennerhag, Yannick Schroecker, Tom Zahavy, Hado van Hasselt, David Silver, Satinder Singh","https://openreview.net/forum?id=b-ny3x071E5","元学习","借用时序差分的自举思想，让元学习器用自己的更新或另一条更新规则来引导自己。","元优化难，是因为外层目标要穿过整个内层训练；自举把这个长程目标拆开了。","想法来自经典 RL，却打开了元学习里一条以前没人走的路。"),
P("ICLR","2022","Outstanding Paper Honorable Mention","Understanding over-squashing and bottlenecks on graphs via curvature","Jake Topping, Francesco Di Giovanni, Benjamin Paul Chamberlain, Xiaowen Dong, Michael M. Bronstein","https://openreview.net/forum?id=7UmjRGzp-A","图神经网络","用边上的组合曲率刻画消息传递里的过挤压，并按曲率重连图来缓解。","远距离信息传不过来，不只是层数不够，负曲率的边会把消息挤扁。","它把一句经验抱怨变成几何命题，重连图也就有了依据。"),
P("ICLR","2022","Outstanding Paper Honorable Mention","Efficiently Modeling Long Sequences with Structured State Spaces","Albert Gu, Karan Goel, Christopher Ré","https://openreview.net/forum?id=uYLFoz1vlAC","长序列模型","提出 S4，给状态空间模型一套可计算的参数化，用来建模长程依赖。","长序列不一定要继续给 Transformer 做手术，被放下的状态空间模型也能算得动。","它在 Transformer 几乎一统序列模型时，认真复活了另一条架构路线。"),
P("ICLR","2022","Outstanding Paper Honorable Mention","PiCO: Contrastive Label Disambiguation for Partial Label Learning","Haobo Wang, Ruixuan Xiao, Yixuan Li, Lei Feng, Gang Niu, Gang Chen, Junbo Zhao","https://openreview.net/forum?id=EhYjZy6e1gJ","部分标签学习","用对比学习和原型一起做标签消歧，把表示学习和消歧放进同一个框架。","候选标签集合既污染监督，也污染表示；两件事分开修，谁也修不利索。","问题来自真实标注，理论用 EM 解释框架，而不是只报一个新的损失。"),
P("ICLR","2023","Outstanding Paper","Universal Few-shot Learning of Dense Prediction Tasks with Visual Token Matching","Donggyun Kim, Jinwoo Kim, Seongwoong Cho, Chong Luo, Seunghoon Hong","https://openreview.net/forum?id=88nT0j5jAn","稠密预测","用视觉 token 匹配把分割、深度、边缘和关键点收成同一个少样本模型。","稠密任务看起来各写各的头，匹配局部 token 之后可以共用一条路。","它不是再刷一个分割榜，而是追问这些任务到底能不能共用一个少样本机制。"),
P("ICLR","2023","Outstanding Paper","Rethinking the Expressive Power of GNNs via Graph Biconnectivity","Bohang Zhang, Shengjie Luo, Liwei Wang, Di He","https://openreview.net/forum?id=r9hNv76KoT3","图神经网络","用双连通性衡量 GNN 表达力，并利用节点间距离补上现有模型分不开的图。","WL 测试分得开的图，在桥和割点这种结构上仍可能被 GNN 看成一样。","表达力论文很多，这篇把指标换成了有实际含义的拓扑性质。"),
P("ICLR","2023","Outstanding Paper","DreamFusion: Text-to-3D using 2D Diffusion","Ben Poole, Ajay Jain, Jonathan T. Barron, Ben Mildenhall","https://openreview.net/forum?id=FjNys5c7VyY","文生三维","不收集三维数据，把二维扩散模型的分数蒸馏进一个神经辐射场，从而从文本生成三维物体。","已经会画画的模型，可以被当成三维生成的老师，而不必先有三维训练集。","组件都不新，新在把二维生成和辐射场接成一条能工作的路，随后带出一整条跟随工作。"),
P("ICLR","2023","Outstanding Paper","Emergence of Maps in the Memories of Blind Navigation Agents","Erik Wijmans, Manolis Savva, Irfan Essa, Stefan Lee, Ari S. Morcos, Dhruv Batra","https://openreview.net/forum?id=lTt4KjHSsyl","具身导航","检查只靠非视觉信号导航的智能体，记忆里是否自己长出了地图式的空间表征。","没有被要求建图的智能体，为了走得通，仍可能在记忆里整理出空间结构。","它用认知科学的问题约束实验，论证过程比单点性能更被看重。"),
P("ICLR","2023","Outstanding Paper Honorable Mention","Towards Understanding Ensemble, Knowledge Distillation and Self-Distillation in Deep Learning","Zeyuan Allen-Zhu, Yuanzhi Li","https://openreview.net/forum?id=Uuf2q9TfXGA","知识蒸馏","在多视图数据上证明：不蒸馏时网络会只靠一部分特征，蒸馏能把丢掉的视图捡回来。","集成和蒸馏有效，不一定是因为老师更准，也可能是因为学生被迫看全特征。","它给一个被用滥的技巧一个可以证伪的机制解释。"),
P("ICLR","2023","Outstanding Paper Honorable Mention","Mastering the Game of No-Press Diplomacy via Human-Regularized Reinforcement Learning and Planning","Anton Bakhtin, David J. Wu, Adam Lerer, Jonathan Gray, Athul Paul Jacob, Gabriele Farina, Alexander H. Miller, Noam Brown","https://openreview.net/forum?id=F61FwJTZhb","多智能体博弈","在无通讯外交棋里把均衡搜索和人类行为克隆合在一起，让策略既强又像人会下的棋。","纯自博弈的均衡，人看不懂也接不住；要和人玩，策略必须落在人认得出的那一块。","多人不完全信息博弈几乎没有标准答案，这篇让人和算法真的对上了局。"),
P("ICLR","2023","Outstanding Paper Honorable Mention","On the duality between contrastive and non-contrastive self-supervised learning","Quentin Garrido, Yubei Chen, Adrien Bardes, Laurent Najman, Yann LeCun","https://openreview.net/forum?id=kDEL91Dufpa","自监督学习","指出对比式和非对比式自监督在一定条件下是对偶的，并不是两套无关的经验配方。","看起来相反的两族方法效果接近，是因为它们在优化几乎同一件事。","它把已经分裂的文献收成一个可以互相翻译的框架。"),
P("ICLR","2023","Outstanding Paper Honorable Mention","Conditional Antibody Design as 3D Equivariant Graph Translation","Xiangzhe Kong, Wenbing Huang, Yang Liu","https://openreview.net/forum?id=LFHFQbjxIiP","蛋白质设计","把给定抗原条件下的抗体 CDR 设计写成等变图到图的翻译，同时生成氨基酸和三维构象。","抗体不是一串独立的序列，骨架坐标和残基种类得一起变。","任务定义比模型名字更重要：它把一个湿实验问题收成可学习的条件生成。"),
P("ICLR","2023","Outstanding Paper Honorable Mention","Disentanglement with Biological Constraints: A Theory of Functional Cell Types","James C. R. Whittington, Will Dorrell, Surya Ganguli, Timothy Behrens","https://openreview.net/forum?id=9Z_GfhZnGH","神经科学与解耦","证明非负和能量效率这两条生物约束，足以让线性网络把表征解耦成功能细胞类型。","解耦不一定要靠精心设计的损失，代谢上说得通的约束本身就会把因子分开。","它让机器学习和神经科学共用一个可以证明的命题，而不是互相打比方。"),
P("ICLR","2024","Outstanding Paper","Generalization in diffusion models arises from geometry-adaptive harmonic representations","Zahra Kadkhodaie, Florentin Guth, Eero P. Simoncelli, Stéphane Mallat","https://openreview.net/forum?id=ANvmVS2Yr0","扩散模型理论","用几何自适应的调和表示解释图像扩散模型何时在记训练集、何时开始泛化。","泛化不是多训一会儿就自动出现的，它对应一组会适应图像几何的归纳偏置。","记忆和泛化是生成模型最核心的分界，这篇给了一个可检验的图像侧解释。"),
P("ICLR","2024","Outstanding Paper","Learning Interactive Real-World Simulators","Sherry Yang, Yilun Du, Seyed Kamyar Seyed Ghasemipour, Jonathan Tompson, Leslie Pack Kaelbling, Dale Schuurmans, Pieter Abbeel","https://openreview.net/forum?id=sFyTZEqmUY","机器人世界模型","把不同机器人的数据收成视觉加文本动作的统一界面，训练出一个可交互的真实世界模拟器 UniSim。","机器人基础模型卡住的地方往往是接口，不是再多采一条轨迹。","它把异构机器人数据这个问题正面拆开，而不是在单一平台上刷成功率。"),
P("ICLR","2024","Outstanding Paper","Never Train from Scratch: Fair Comparison of Long-Sequence Models Requires Data-Driven Priors","Ido Amos, Jonathan Berant, Ankit Gupta","https://openreview.net/forum?id=PdaPky8MUn","长序列模型","比较状态空间模型和 Transformer 的长程能力时，发现从零训练会系统性低估 Transformer。","架构对比如果都从随机初始化开始，比的是谁更好训，不是谁更能利用数据里的先验。","它修正的是一整类论文的实验协议，而不只是提出另一个模块。"),
P("ICLR","2024","Outstanding Paper","Protein Discovery with Discrete Walk-Jump Sampling","Nathan C. Frey, Dan Berenberg, Karina Zadorozhny, Joseph Kleinhenz, Julien Lafrance-Vanasse, Isidro Hotzel, Yan Wu, Stephen Ra, Richard Bonneau, Kyunghyun Cho, Andreas Loukas, Vladimir Gligorijevic, Saeed Saremi","https://openreview.net/forum?id=zMPHKOmQNb","抗体设计","为离散蛋白质序列设计 walk-jump 采样，并在体外测了生成抗体的结合。","离散序列不能直接套连续扩散的采样直觉，能量景观和跳跃方式要单独设计。","生成模型论文很少走到湿实验，这篇把计算设计和结合实验放在同一篇里。"),
P("ICLR","2024","Outstanding Paper","Vision Transformers Need Registers","Timothée Darcet, Maxime Oquab, Julien Mairal, Piotr Bojanowski","https://openreview.net/forum?id=2dnO3LLiJ1","视觉 Transformer","发现 ViT 特征图里有高范数的背景伪影，加一组 register token 就能把伪影接走。","模型会把不该出现在图里的全局信息塞进无信息背景块，因为没有别的地方可放。","现象、机制和一行就能加上的修法写在同一篇里，是很完整的研究叙事。"),
P("ICLR","2024","Outstanding Paper Honorable Mention","Amortizing intractable inference in large language models","Edward J. Hu, Moksh Jain, Eric Elmoznino, Younesse Kaddar, Guillaume Lajoie, Yoshua Bengio, Nikolay Malkin","https://openreview.net/forum?id=Ouj6p4ca60","语言模型推断","把自回归解码改写成摊销的贝叶斯推断问题，试图一次学出会从后验里抽样的网络。","逐 token 解码是一种很特别的推断顺序，不是语言建模唯一的概率问答方式。","它提供的是另一条解码问题的提法，评委会看重的是这个问题本身。"),
P("ICLR","2024","Outstanding Paper Honorable Mention","Approximating Nash Equilibria in Normal-Form Games via Stochastic Optimization","Ian Gemp, Luke Marris, Georgios Piliouras","https://openreview.net/forum?id=cc8h3I3V4E","博弈论","把正规型博弈的纳什均衡近似写成可扩展的随机优化。","均衡求解不该只在小矩阵上演示，目标是让优化器能处理更大的博弈。","写得异常清楚，而且推进的是一个老问题的可计算性。"),
P("ICLR","2024","Outstanding Paper Honorable Mention","Beyond Weisfeiler-Lehman: A Quantitative Framework for GNN Expressiveness","Bohang Zhang, Jingchu Gai, Yiheng Du, Qiwei Ye, Di He, Liwei Wang","https://openreview.net/forum?id=HSKaGOi7Ar","图神经网络","用同态计数给 GNN 表达力一个定量框架，补上 WL 测试只能回答能不能分开的缺口。","两个模型都通过了同一级 WL，仍可能差很多，差多少需要另一把尺子。","表达力文献几乎只报分离能力，这篇把多少换成了可比较的量。"),
P("ICLR","2024","Outstanding Paper Honorable Mention","Flow Matching on General Geometries","Ricky T. Q. Chen, Yaron Lipman","https://openreview.net/forum?id=g7ohDlTITL","生成模型","把 flow matching 推广到一般黎曼流形，使生成过程能沿几何本身走。","数据如果住在球、环面或旋转群上，硬嵌入欧氏空间会让路径绕远。","算法能算，实验覆盖多种几何，写作也把条件讲清楚了。"),
P("ICLR","2024","Outstanding Paper Honorable Mention","Is ImageNet worth 1 video? Learning strong image encoders from 1 long unlabelled video","Shashanka Venkataramanan, Mamshad Nayeem Rizve, Joao Carreira, Yuki M. Asano, Yannis Avrithis","https://openreview.net/forum?id=Yen1lGns2o","自监督视觉","用一条很长的无标注视频学习图像编码器，把连续视频当成图像预训练的数据来源。","静态图数据集的多样性，有一部分可以从一条视频的时间连续性里长出来。","它同时贡献了一种数据和一种学法，问题也问得很锋利。"),
P("ICLR","2024","Outstanding Paper Honorable Mention","Meta Continual Learning Revisited: Implicitly Enhancing Online Hessian Approximation via Variance Reduction","Yichen Wu, Long-Kai Huang, Renzhen Wang, Deyu Meng, Ying Wei","https://openreview.net/forum?id=TpD2aG1h0D","持续学习","用方差缩减改进元持续学习里的在线 Hessian 近似，并给出后悔界。","元学习和持续学习叠在一起时，二阶信息的噪声会先于算法本身崩掉。","经验方法配了后悔分析，不是只在一个划分上更好。"),
P("ICLR","2024","Outstanding Paper Honorable Mention","Model Tells You What to Discard: Adaptive KV Cache Compression for LLMs","Suyu Ge, Yunan Zhang, Liyuan Liu, Minjia Zhang, Jiawei Han, Jianfeng Gao","https://openreview.net/forum?id=uNrFpDPMyo","推理效率","让模型自己决定 KV cache 里哪些 token 可以丢，压缩不必再训练。","注意力并不同等依赖所有历史 token，缓存可以跟着这个事实变短。","问题是部署里真实的显存瓶颈，方法又轻到可以插进已有模型。"),
P("ICLR","2024","Outstanding Paper Honorable Mention","Proving Test Set Contamination in Black-Box Language Models","Yonatan Oren, Nicole Meister, Niladri S. Chatterji, Faisal Ladhak, Tatsunori Hashimoto","https://openreview.net/forum?id=KS8mIvetg2","评测污染","给黑盒语言模型一个可检验的办法，判断某份有监督数据集是否进过训练。","榜上的高分如果来自背题，黑盒 API 也会留下可统计的痕迹。","方法简单，打中的却是整个评测体系正在失去可信度的那一点。"),
P("ICLR","2024","Outstanding Paper Honorable Mention","Robust agents learn causal world models","Jonathan Richens, Tom Everitt","https://openreview.net/forum?id=pOoKI3ouv1","因果与智能体","证明若智能体要在分布变化下保持稳健决策，它学到的世界模型必须带有因果关系。","只拟合观测相关就够用的策略，换一个干预就会碎。","它把因果从口号收成稳健决策的必要条件。"),
P("ICLR","2024","Outstanding Paper Honorable Mention","The mechanistic basis of data dependence and abrupt learning in an in-context classification task","Gautam Reddy","https://openreview.net/forum?id=aN4Jf6Cx69","上下文学习","在一个可控的上下文分类任务里，拆开数据依赖和突然学会这两件事的机制。","上下文学习和权重里的学习何时切换，可以在小任务里看清楚，而不是只在大模型里描述。","现象正热，文章却把机制写成可以逐步核对的分析。"),
P("ICLR","2024","Outstanding Paper Honorable Mention","Towards a statistical theory of data selection under weak supervision","Germain Kolossov, Andrea Montanari, Pulkit Tandon","https://openreview.net/forum?id=HhfcNgQn6p","数据筛选","在弱监督下给出数据子集选择的统计理论，并指出流行筛选指标会在哪里失效。","数据筛选如果只按一个代理分数排序，选出来的集合可能并不是统计上该留的。","它给正在变成默认流程的数据工程一个会失败的条件。"),
P("ICLR","2025","Outstanding Paper","Safety Alignment Should be Made More Than Just a Few Tokens Deep","Xiangyu Qi, Ashwinee Panda, Kaifeng Lyu, Xiao Ma, Subhrajit Roy, Ahmad Beirami, Prateek Mittal, Peter Henderson","https://openreview.net/forum?id=6Mxhg9PtDE","安全对齐","表明常见安全对齐大多只改动回答开头的少数 token，稍一改前缀，拒绝就会退回去。","对齐如果只写在句子起手式里，它就不是模型的稳定策略，而是一个很浅的格式。","它把安全对齐的失败从案例收成一个可定位的深度问题。"),
P("ICLR","2025","Outstanding Paper","Learning Dynamics of LLM Finetuning","Yi Ren, Danica J. Sutherland","https://openreview.net/forum?id=tPNHOoZFl9","微调动力学","分析大模型微调时参数和预测如何一起变，用来解释遗忘、幻觉式偏移等现象从哪来。","微调的副作用不一定是数据脏，也可能是学习动力学本身把概率质量推走了。","在人人微调的年份，它去写动力学而不是再交一个微调配方。"),
P("ICLR","2025","Outstanding Paper","AlphaEdit: Null-Space Constrained Model Editing for Language Models","Junfeng Fang, Houcheng Jiang, Kun Wang, Yunshan Ma, Jie Shi, Xiang Wang, Xiangnan He, Tat-Seng Chua","https://openreview.net/forum?id=HvSytvg3Jh","模型编辑","把知识编辑投影到与原有知识零空间相关的方向上，减少改一条事实时撞坏其他事实。","编辑失败常常是因为更新方向和旧知识重叠，而不是因为编辑量不够大。","它用一个线性代数约束把定位与编辑和灾难性遗忘接上了。"),
P("ICLR","2025","Outstanding Paper Honorable Mention","Data Shapley in One Training Run","Jiachen T. Wang, Prateek Mittal, Dawn Song, Ruoxi Jia","https://openreview.net/forum?id=HD6bWcj87Y","数据估值","把数据 Shapley 值的估计收进一次训练，而不必为每个子集反复重训。","数据估值在概念上很对，贵在每次都要重训；能跟着一次训练记下来，方法才用得起。","它移走的是数据归因里最挡路的计算假设。"),
P("ICLR","2025","Outstanding Paper Honorable Mention","SAM 2: Segment Anything in Images and Videos","Nikhila Ravi, Valentin Gabeur, Yuan-Ting Hu, Ronghang Hu, Chaitanya Ryali, Tengyu Ma, Haitham Khedr, Roman Rädle, Chloe Rolland, Laura Gustafson, Eric Mintun, Junting Pan, Kalyan Vasudev Alwala, Nicolas Carion, Chao-Yuan Wu, Ross Girshick, Piotr Dollár, Christoph Feichtenhofer","https://openreview.net/forum?id=Ha6RTeWMd0","视频分割","把可提示的分割从单张图扩到视频，用记忆模块在时间上保持同一个对象。","图像里点一下就能分割，视频里还得记住上一帧的对象没有换人。","数据和交互方式一起设计，使一个已经重要的基础模型真正进入时间维度。"),
P("ICLR","2025","Outstanding Paper Honorable Mention","Faster Cascades via Speculative Decoding","Harikrishna Narasimhan, Wittawat Jitkrittum, Ankit Singh Rawat, Seungyeon Kim, Neha Gupta, Aditya Krishna Menon, Sanjiv Kumar","https://openreview.net/forum?id=vo9t20wsmd","推理效率","把推测解码用到大小模型级联上，让小模型先写、大模型只在必要时接手。","级联省的是调用次数，推测解码省的是逐 token 等待，两件事可以叠在同一条生成路径上。","它把两篇文献里各自正确的节省合成了一个系统。"),
P("ICLR","2026","Outstanding Paper","LLMs Get Lost In Multi-Turn Conversation","Philippe Laban, Hiroaki Hayashi, Yingbo Zhou, Jennifer Neville","https://openreview.net/forum?id=VKGTGGcwl6","多轮对话","做了一套可扩展的多轮评测，测量指令分几轮、且一开始没说清时，模型完成任务的能力怎么掉。","训练几乎都是单轮补全，使用几乎都是多轮；落差就出现在指令被拆开的时候。","评委会写明实验设计突出，而且问题就是模型真实被使用的方式。"),
P("ICLR","2026","Outstanding Paper","Transformers are Inherently Succinct","Pascal Bergsträßer, Ryan Cotterell, Anthony Widjaja Lin","https://openreview.net/forum?id=Yxz92UuPLQ","架构理论","从简洁性比较 Transformer 和 RNN：表达同一个概念，Transformer 可以用短得多的程序。","表达力如果只问能不能算，会漏掉用多长的描述才能算出来。","理论命题清楚，而且给了经验工作一个可以继续测的架构问题。"),
P("ICLR","2026","Outstanding Paper Honorable Mention","The Polar Express: Optimal Matrix Sign Methods and their Application to the Muon Algorithm","Noah Amsel, David Persson, Christopher Musco, Robert M. Gower","https://openreview.net/forum?id=yRtgZ1K8hO","优化器","用逼近论给极分解设计在低精度 GPU 上更合适的多项式，并接到 Muon 优化器。","Muon 里最贵的矩阵符号函数不该靠通用迭代，多项式次数和硬件算术要一起设计。","经验提升不一定巨大，但方法是对着一个正在被广泛使用的优化器做的。"),
P("ICLR",2024,"Test of Time","Auto-Encoding Variational Bayes","Diederik P. Kingma, Max Welling","https://arxiv.org/abs/1312.6114","变分推断","提出用重参数化梯度训练变分自编码器。","它让深度潜变量模型第一次可以稳定地用随机梯度来学。","2024 年被选为 ICLR 时间检验奖，因为整条深度生成模型的路线都还站在这篇上。",True,2014),
P("ICLR",2024,"Test of Time Runner-up","Intriguing properties of neural networks","Christian Szegedy, Wojciech Zaremba, Ilya Sutskever, Joan Bruna, Dumitru Erhan, Ian Goodfellow, Rob Fergus","https://arxiv.org/abs/1312.6199","对抗样本","展示深度网络对微小扰动会给出高置信的错误预测。","网络的决策边界可以离数据点近到人眼看不出来。","2024 年作为时间检验入围，对抗鲁棒性这条线从这里算起。",True,2014),
P("ICLR",2025,"Test of Time","Adam: A Method for Stochastic Optimization","Diederik P. Kingma, Jimmy Ba","https://arxiv.org/abs/1412.6980","优化","提出结合一阶矩和二阶矩的自适应随机优化方法 Adam。","每个参数用自己的梯度尺度来走，训练就不必手调一套全局学习率。","2025 年的时间检验奖。它已经是深度学习训练的默认优化器。",True,2015),
P("ICLR",2025,"Test of Time Runner-up","Neural Machine Translation by Jointly Learning to Align and Translate","Dzmitry Bahdanau, Kyunghyun Cho, Yoshua Bengio","https://arxiv.org/abs/1409.0473","注意力","在神经机器翻译里联合学习对齐和翻译，引入加性注意力。","解码不该把整句压成一个固定向量，而该在每一步回去看该看的源词。","2025 年时间检验入围。后来的 Transformer 仍在回答同一件对齐的事。",True,2015),
P("ICLR",2026,"Test of Time","Unsupervised Representation Learning with Deep Convolutional Generative Adversarial Networks","Alec Radford, Luke Metz, Soumith Chintala","https://arxiv.org/abs/1511.06434","生成模型","DCGAN 证明卷积 GAN 可以合成多样、看起来真实的图像。","生成模型不是只能在小数据上玩，架构约束对了就能画出复杂图像。","2026 年官方时间检验奖。图像生成这条线的起点之一。",True,2016),
P("ICLR",2026,"Test of Time","Continuous control with deep reinforcement learning","Timothy P. Lillicrap, Jonathan J. Hunt, Alexander Pritzel, Nicolas Heess, Tom Erez, Yuval Tassa, David Silver, Daan Wierstra","https://arxiv.org/abs/1509.02971","强化学习","提出 DDPG，把确定性演员-评论家和 DQN 的稳定技巧合在一起，直接输出连续动作。","连续控制不必先把动作离散化，也不必先手工做状态特征。","2026 年官方时间检验奖。深度强化学习走进机器人，这篇是入口。",True,2016),
)

from records_ml import ML_PAPERS
from records_nlp import NLP_PAPERS
PAPERS.extend(ML_PAPERS)
PAPERS.extend(NLP_PAPERS)

for row in PAPERS:
    row["year"] = int(row["year"])

if __name__ == "__main__":
    OUT.write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in PAPERS), encoding="utf-8")
    print(f"wrote {len(PAPERS)} rows")
