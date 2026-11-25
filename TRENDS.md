# 五年里，获奖论文在往哪边偏

下面不是预言，是把这份清单里的获奖论文按年摊开之后，能看见的几条线。时间检验奖不算进当年，它们是回看十年前的工作。NeurIPS 2026 还没公布，所以 2026 年缺了机器学习这边最大的一场。

## 2022：生成模型开始被当成基础设施

这一年的奖还不是「聊天」。扩散模型同时出现在方法、理论和数据上。NeurIPS 把 Imagen（*Photorealistic Text-to-Image Diffusion Models with Deep Language Understanding*）和 *Elucidating the Design Space of Diffusion-Based Generative Models* 放在一起：一边是能用的文生图，一边是把一堆公式收成同一张设计表。ICLR 的 Analytic-DPM 则把反向过程里的方差写成闭式。生成模型从「能画出图」变成「值得被分析的对象」。

同一年，规模被重新算账。Chinchilla（*An empirical analysis of compute-optimal large language model training*）说固定算力下不该只堆参数；*Beyond neural scaling laws* 说数据不是同质的，剪掉差的样本可以改掉幂律。LAION-5B 则把图文数据本身做成公共品。

具身没有被生成模型盖住。ProcTHOR 和 MineDojo 都在奖生成式数据之前，先奖「有没有一个能无限变的世界」。S4 是另一条线：长序列不一定继续给 Transformer 做手术。

所以「2022 是生成式奠基、扩散模型」大致对，但更准确的说法是：扩散、缩放和开放世界同时被当成基础问题，而不是只有画图。

## 2023：对齐成为默认后训练，涌现被要求拿出证据

最清楚的一篇是 DPO（*Direct Preference Optimization*）。它把「先训奖励、再跑强化学习」收成一次分类式微调。ICML 的语言模型水印是同一股潮流的另一面：生成文本开始需要被归因。

「涌现」也在这一年被拆开。*Are Emergent Abilities of Large Language Models a Mirage?* 说很多突然出现的能力是指标不连续造成的。这和 DPO 放在一起读，口味就出来了：社区既急着让模型听话，也开始怀疑自己讲的故事。

机制解释没有只停在大模型。ACL 的 DAAM 用交叉注意力去看扩散模型；ICLR 的蒸馏论文在多视图数据上解释集成为什么有用。DreamFusion 则说明二维扩散已经可以被当成三维生成的老师。

不要把 2023 收成只有对齐。ICML 的 D-Adaptation、NeurIPS 的一次训练隐私审计、AAAI 的逆强化学习误设，都是在问：你以为已经解决的工具，前提是不是错的。

## 2024：多模态想共用一个骨架，语言学问题回到主会

多模态这一年不是「再加一个模态」，而是想共用语言建模的训练方式。ICML 的 VideoPoet 用解码器语言模型生成视频，Genie 从没有动作标签的视频里长出可交互环境，ICLR 的 UniSim 把不同机器人收成视觉加文本动作。NeurIPS 的 VAR 则改了图像自回归的单位：不是下一个图块，是下一个尺度。整流流放大到高分辨率（*Scaling Rectified Flow Transformers*）说明扩散的配方也在换骨架。

「自我进化」不是这一年的主线。更接近的是世界模型和交互环境：Genie、UniSim，以及 NAACL 的 *Teaching Language Models to Self-Improve through Interactive Demonstrations*。自我改进在，但还是一条小线，不是获奖名单的中心。

语言学确实回来了，而且是以质疑模型的方式回来。ACL 的 *Mission: Impossible Language Models* 用人类不会的语言去探归纳偏置；*Why are Sensitive Functions Hard for Transformers?* 把形式语言的难度和架构绑在一起；甲骨文扩散是古文字和生成模型的一次正面相遇。OLMo 和 Dolma 则把「开放」从口号做成可核对的训练记录。

## 2025：安全要看深度，效率要长在结构里，同质化被当成风险

安全对齐不再满足于「模型会拒绝」。ICLR 的 *Safety Alignment Should be Made More Than Just a Few Tokens Deep* 说常见对齐只写在回答开头的几个 token 上。ACL 的 *Language Models Resist Alignment* 从压缩的角度说，预训练里的倾向不容易被微调抹掉。

效率奖给的是能进训练、而不只是推理技巧的结构。NeurIPS 的门控注意力把「加门」拆开做实验；ACL 的 Native Sparse Attention 强调稀疏必须在硬件上真的训得动。ICLR 的推测解码级联是同一年更靠系统的一篇。

同质化被单独拿出来。NeurIPS 的 *Artificial Hivemind* 用开放式真实提问看模型内部和模型之间如何给出几乎一样的回答。这和「2025 警惕同质化」是对得上的，而且它是数据集轨道的最佳论文，不是附属话题。

还有一条 2025 特有的怀疑：*Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model?* 问强化学习是不是只是把基座里已有的解抽取得更频繁。推理模型最热的时候，获奖名单里留了这个问号。

## 2026：生成式的默认假设被拆开，古典问题接回来

草稿里的「逻辑、因果、具身重新结合」有一部分是对的，但不是全部。更稳的说法是：社区开始拆掉生成式模型这几年的默认假设，并把拆下来的洞重新接到旧问题上。

默认假设之一是「任意顺序一定更好」。ICML 的 *The Flexibility Trap* 说扩散语言模型在一般推理上会利用这个自由绕开真正难的 token。ICLR 的 *LLMs Get Lost In Multi-Turn Conversation* 拆的是另一个默认：训练是单轮的，使用却是多轮的。

理论重新变得具体。*Transformers are Inherently Succinct* 不问能不能算，问用多短的描述才能算。ACL 的 *Characterizing the Expressivity of Local Attention* 和未完成体悖论（*The Imperfective Paradox in Large Language Models*）把表达力和语言学的老问题放回主会。EMNLP 的 DiscoTrace 比较人和模型回答问题时的策略，而不是只比最后一句。

因果和具身也在 AAAI 的杰出论文里重新出现：动力系统的因果结构学习，以及 ReconVLA 把重建式感知接回机器人动作。这支持「具身和因果回来了」，但它们是和效率、欺骗探针、对齐的两用性（*The Alignment Community is Unintentionally Building a Censor's Toolkit*）并列的，不是取代了后两者。

2026 年还缺 NeurIPS。上面这些判断等那场的最佳论文出来之后，可能要改。

## 如果只想练口味，每年先读这几篇

- 2022：Chinchilla；Elucidating the Design Space of Diffusion Models；S4
- 2023：DPO；Are Emergent Abilities a Mirage?；DreamFusion
- 2024：Mission: Impossible Language Models；Genie；VAR
- 2025：Safety Alignment … a Few Tokens Deep；Artificial Hivemind；Native Sparse Attention
- 2026：The Flexibility Trap；LLMs Get Lost In Multi-Turn Conversation；DiscoTrace
