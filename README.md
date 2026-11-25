# 顶会最佳论文（2022–2026）

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

# ICLR

## 2026

### Outstanding Paper

* **LLMs Get Lost In Multi-Turn Conversation**
  [论文](https://openreview.net/forum?id=VKGTGGcwl6) · Philippe Laban, Hiroaki Hayashi, Yingbo Zhou, Jennifer Neville
  做了一套可扩展的多轮评测，测量指令分几轮、且一开始没说清时，模型完成任务的能力怎么掉。

* **Transformers are Inherently Succinct**
  [论文](https://openreview.net/forum?id=Yxz92UuPLQ) · Pascal Bergsträßer, Ryan Cotterell, Anthony Widjaja Lin
  从简洁性比较 Transformer 和 RNN：表达同一个概念，Transformer 可以用短得多的程序。

### Outstanding Paper Honorable Mention

* **The Polar Express: Optimal Matrix Sign Methods and their Application to the Muon Algorithm**
  [论文](https://openreview.net/forum?id=yRtgZ1K8hO) · Noah Amsel, David Persson, Christopher Musco, Robert M. Gower
  用逼近论给极分解设计在低精度 GPU 上更合适的多项式，并接到 Muon 优化器。

## 2025

### Outstanding Paper

* **Safety Alignment Should be Made More Than Just a Few Tokens Deep**
  [论文](https://openreview.net/forum?id=6Mxhg9PtDE) · Xiangyu Qi, Ashwinee Panda, Kaifeng Lyu, Xiao Ma, Subhrajit Roy, Ahmad Beirami, Prateek Mittal, Peter Henderson
  表明常见安全对齐大多只改动回答开头的少数 token，稍一改前缀，拒绝就会退回去。

* **Learning Dynamics of LLM Finetuning**
  [论文](https://openreview.net/forum?id=tPNHOoZFl9) · Yi Ren, Danica J. Sutherland
  分析大模型微调时参数和预测如何一起变，用来解释遗忘、幻觉式偏移等现象从哪来。

* **AlphaEdit: Null-Space Constrained Model Editing for Language Models**
  [论文](https://openreview.net/forum?id=HvSytvg3Jh) · Junfeng Fang, Houcheng Jiang, Kun Wang, Yunshan Ma, Jie Shi, Xiang Wang, Xiangnan He, Tat-Seng Chua
  把知识编辑投影到与原有知识零空间相关的方向上，减少改一条事实时撞坏其他事实。

### Outstanding Paper Honorable Mention

* **Data Shapley in One Training Run**
  [论文](https://openreview.net/forum?id=HD6bWcj87Y) · Jiachen T. Wang, Prateek Mittal, Dawn Song, Ruoxi Jia
  把数据 Shapley 值的估计收进一次训练，而不必为每个子集反复重训。

* **SAM 2: Segment Anything in Images and Videos**
  [论文](https://openreview.net/forum?id=Ha6RTeWMd0) · Nikhila Ravi, Valentin Gabeur, Yuan-Ting Hu, Ronghang Hu, Chaitanya Ryali, Tengyu Ma 等
  把可提示的分割从单张图扩到视频，用记忆模块在时间上保持同一个对象。

* **Faster Cascades via Speculative Decoding**
  [论文](https://openreview.net/forum?id=vo9t20wsmd) · Harikrishna Narasimhan, Wittawat Jitkrittum, Ankit Singh Rawat, Seungyeon Kim, Neha Gupta, Aditya Krishna Menon, Sanjiv Kumar
  把推测解码用到大小模型级联上，让小模型先写、大模型只在必要时接手。

## 2024

### Outstanding Paper

* **Generalization in diffusion models arises from geometry-adaptive harmonic representations**
  [论文](https://openreview.net/forum?id=ANvmVS2Yr0) · Zahra Kadkhodaie, Florentin Guth, Eero P. Simoncelli, Stéphane Mallat
  用几何自适应的调和表示解释图像扩散模型何时在记训练集、何时开始泛化。

* **Learning Interactive Real-World Simulators**
  [论文](https://openreview.net/forum?id=sFyTZEqmUY) · Sherry Yang, Yilun Du, Seyed Kamyar Seyed Ghasemipour, Jonathan Tompson, Leslie Pack Kaelbling, Dale Schuurmans, Pieter Abbeel
  把不同机器人的数据收成视觉加文本动作的统一界面，训练出一个可交互的真实世界模拟器 UniSim。

* **Never Train from Scratch: Fair Comparison of Long-Sequence Models Requires Data-Driven Priors**
  [论文](https://openreview.net/forum?id=PdaPky8MUn) · Ido Amos, Jonathan Berant, Ankit Gupta
  比较状态空间模型和 Transformer 的长程能力时，发现从零训练会系统性低估 Transformer。

* **Protein Discovery with Discrete Walk-Jump Sampling**
  [论文](https://openreview.net/forum?id=zMPHKOmQNb) · Nathan C. Frey, Dan Berenberg, Karina Zadorozhny, Joseph Kleinhenz, Julien Lafrance-Vanasse, Isidro Hotzel 等
  为离散蛋白质序列设计 walk-jump 采样，并在体外测了生成抗体的结合。

* **Vision Transformers Need Registers**
  [论文](https://openreview.net/forum?id=2dnO3LLiJ1) · Timothée Darcet, Maxime Oquab, Julien Mairal, Piotr Bojanowski
  发现 ViT 特征图里有高范数的背景伪影，加一组 register token 就能把伪影接走。

### Outstanding Paper Honorable Mention

* **Amortizing intractable inference in large language models**
  [论文](https://openreview.net/forum?id=Ouj6p4ca60) · Edward J. Hu, Moksh Jain, Eric Elmoznino, Younesse Kaddar, Guillaume Lajoie, Yoshua Bengio, Nikolay Malkin
  把自回归解码改写成摊销的贝叶斯推断问题，试图一次学出会从后验里抽样的网络。

* **Approximating Nash Equilibria in Normal-Form Games via Stochastic Optimization**
  [论文](https://openreview.net/forum?id=cc8h3I3V4E) · Ian Gemp, Luke Marris, Georgios Piliouras
  把正规型博弈的纳什均衡近似写成可扩展的随机优化。

* **Beyond Weisfeiler-Lehman: A Quantitative Framework for GNN Expressiveness**
  [论文](https://openreview.net/forum?id=HSKaGOi7Ar) · Bohang Zhang, Jingchu Gai, Yiheng Du, Qiwei Ye, Di He, Liwei Wang
  用同态计数给 GNN 表达力一个定量框架，补上 WL 测试只能回答能不能分开的缺口。

* **Flow Matching on General Geometries**
  [论文](https://openreview.net/forum?id=g7ohDlTITL) · Ricky T. Q. Chen, Yaron Lipman
  把 flow matching 推广到一般黎曼流形，使生成过程能沿几何本身走。

* **Is ImageNet worth 1 video? Learning strong image encoders from 1 long unlabelled video**
  [论文](https://openreview.net/forum?id=Yen1lGns2o) · Shashanka Venkataramanan, Mamshad Nayeem Rizve, Joao Carreira, Yuki M. Asano, Yannis Avrithis
  用一条很长的无标注视频学习图像编码器，把连续视频当成图像预训练的数据来源。

* **Meta Continual Learning Revisited: Implicitly Enhancing Online Hessian Approximation via Variance Reduction**
  [论文](https://openreview.net/forum?id=TpD2aG1h0D) · Yichen Wu, Long-Kai Huang, Renzhen Wang, Deyu Meng, Ying Wei
  用方差缩减改进元持续学习里的在线 Hessian 近似，并给出后悔界。

* **Model Tells You What to Discard: Adaptive KV Cache Compression for LLMs**
  [论文](https://openreview.net/forum?id=uNrFpDPMyo) · Suyu Ge, Yunan Zhang, Liyuan Liu, Minjia Zhang, Jiawei Han, Jianfeng Gao
  让模型自己决定 KV cache 里哪些 token 可以丢，压缩不必再训练。

* **Proving Test Set Contamination in Black-Box Language Models**
  [论文](https://openreview.net/forum?id=KS8mIvetg2) · Yonatan Oren, Nicole Meister, Niladri S. Chatterji, Faisal Ladhak, Tatsunori Hashimoto
  给黑盒语言模型一个可检验的办法，判断某份有监督数据集是否进过训练。

* **Robust agents learn causal world models**
  [论文](https://openreview.net/forum?id=pOoKI3ouv1) · Jonathan Richens, Tom Everitt
  证明若智能体要在分布变化下保持稳健决策，它学到的世界模型必须带有因果关系。

* **The mechanistic basis of data dependence and abrupt learning in an in-context classification task**
  [论文](https://openreview.net/forum?id=aN4Jf6Cx69) · Gautam Reddy
  在一个可控的上下文分类任务里，拆开数据依赖和突然学会这两件事的机制。

* **Towards a statistical theory of data selection under weak supervision**
  [论文](https://openreview.net/forum?id=HhfcNgQn6p) · Germain Kolossov, Andrea Montanari, Pulkit Tandon
  在弱监督下给出数据子集选择的统计理论，并指出流行筛选指标会在哪里失效。

## 2023

### Outstanding Paper

* **Universal Few-shot Learning of Dense Prediction Tasks with Visual Token Matching**
  [论文](https://openreview.net/forum?id=88nT0j5jAn) · Donggyun Kim, Jinwoo Kim, Seongwoong Cho, Chong Luo, Seunghoon Hong
  用视觉 token 匹配把分割、深度、边缘和关键点收成同一个少样本模型。

* **Rethinking the Expressive Power of GNNs via Graph Biconnectivity**
  [论文](https://openreview.net/forum?id=r9hNv76KoT3) · Bohang Zhang, Shengjie Luo, Liwei Wang, Di He
  用双连通性衡量 GNN 表达力，并利用节点间距离补上现有模型分不开的图。

* **DreamFusion: Text-to-3D using 2D Diffusion**
  [论文](https://openreview.net/forum?id=FjNys5c7VyY) · Ben Poole, Ajay Jain, Jonathan T. Barron, Ben Mildenhall
  不收集三维数据，把二维扩散模型的分数蒸馏进一个神经辐射场，从而从文本生成三维物体。

* **Emergence of Maps in the Memories of Blind Navigation Agents**
  [论文](https://openreview.net/forum?id=lTt4KjHSsyl) · Erik Wijmans, Manolis Savva, Irfan Essa, Stefan Lee, Ari S. Morcos, Dhruv Batra
  检查只靠非视觉信号导航的智能体，记忆里是否自己长出了地图式的空间表征。

### Outstanding Paper Honorable Mention

* **Towards Understanding Ensemble, Knowledge Distillation and Self-Distillation in Deep Learning**
  [论文](https://openreview.net/forum?id=Uuf2q9TfXGA) · Zeyuan Allen-Zhu, Yuanzhi Li
  在多视图数据上证明：不蒸馏时网络会只靠一部分特征，蒸馏能把丢掉的视图捡回来。

* **Mastering the Game of No-Press Diplomacy via Human-Regularized Reinforcement Learning and Planning**
  [论文](https://openreview.net/forum?id=F61FwJTZhb) · Anton Bakhtin, David J. Wu, Adam Lerer, Jonathan Gray, Athul Paul Jacob, Gabriele Farina, Alexander H. Miller, Noam Brown
  在无通讯外交棋里把均衡搜索和人类行为克隆合在一起，让策略既强又像人会下的棋。

* **On the duality between contrastive and non-contrastive self-supervised learning**
  [论文](https://openreview.net/forum?id=kDEL91Dufpa) · Quentin Garrido, Yubei Chen, Adrien Bardes, Laurent Najman, Yann LeCun
  指出对比式和非对比式自监督在一定条件下是对偶的，并不是两套无关的经验配方。

* **Conditional Antibody Design as 3D Equivariant Graph Translation**
  [论文](https://openreview.net/forum?id=LFHFQbjxIiP) · Xiangzhe Kong, Wenbing Huang, Yang Liu
  把给定抗原条件下的抗体 CDR 设计写成等变图到图的翻译，同时生成氨基酸和三维构象。

* **Disentanglement with Biological Constraints: A Theory of Functional Cell Types**
  [论文](https://openreview.net/forum?id=9Z_GfhZnGH) · James C. R. Whittington, Will Dorrell, Surya Ganguli, Timothy Behrens
  证明非负和能量效率这两条生物约束，足以让线性网络把表征解耦成功能细胞类型。

## 2022

### Outstanding Paper

* **Analytic-DPM: an Analytic Estimate of the Optimal Reverse Variance in Diffusion Probabilistic Models**
  [论文](https://openreview.net/forum?id=0xiJLKH-ufZ) · Fan Bao, Chongxuan Li, Jun Zhu, Bo Zhang
  给出扩散模型最优反向方差和对应 KL 的解析形式，并用预训练 score 做免训练估计。

* **Hyperparameter Tuning with Renyi Differential Privacy**
  [论文](https://openreview.net/forum?id=-70L8lpp9DF) · Nicolas Papernot, Thomas Steinke
  指出反复调超参会把隐私账本算漏，并在 Rényi 差分隐私里给搜索过程补上保证。

* **Learning Strides in Convolutional Neural Networks**
  [论文](https://openreview.net/forum?id=M752z9FKJP) · Rachid Riad, Olivier Teboul, David Grangier, Neil Zeghidour
  提出 DiffStride，在傅里叶域里学习下采样窗口，让步长变成可训练的。

* **Expressiveness and Approximation Properties of Graph Neural Networks**
  [论文](https://openreview.net/forum?id=wIzUeM3TAU) · Floris Geerts, Juan L. Reutter
  用张量语言重写 GNN 的表达力问题，把分离能力接到 Weisfeiler-Leman 和树宽上。

* **Comparing Distributions by Measuring Differences that Affect Decision Making**
  [论文](https://openreview.net/forum?id=KB5onONJIAU) · Shengjia Zhao, Abhishek Sinha, Yutong He, Aidan Perreault, Jiaming Song, Stefano Ermon
  定义一类由决策损失诱导的差异，用来比较两个分布在具体决策上差多少。

* **Neural Collapse Under MSE Loss: Proximity to and Dynamics on the Central Path**
  [论文](https://openreview.net/forum?id=w1UbdvWH_R3) · X.Y. Han, Vardan Papyan, David L. Donoho
  在均方误差下拆开神经坍缩，并沿一条中心路径写出可预测的动力学。

* **Bootstrapped Meta-Learning**
  [论文](https://openreview.net/forum?id=b-ny3x071E5) · Sebastian Flennerhag, Yannick Schroecker, Tom Zahavy, Hado van Hasselt, David Silver, Satinder Singh
  借用时序差分的自举思想，让元学习器用自己的更新或另一条更新规则来引导自己。

### Outstanding Paper Honorable Mention

* **Understanding over-squashing and bottlenecks on graphs via curvature**
  [论文](https://openreview.net/forum?id=7UmjRGzp-A) · Jake Topping, Francesco Di Giovanni, Benjamin Paul Chamberlain, Xiaowen Dong, Michael M. Bronstein
  用边上的组合曲率刻画消息传递里的过挤压，并按曲率重连图来缓解。

* **Efficiently Modeling Long Sequences with Structured State Spaces**
  [论文](https://openreview.net/forum?id=uYLFoz1vlAC) · Albert Gu, Karan Goel, Christopher Ré
  提出 S4，给状态空间模型一套可计算的参数化，用来建模长程依赖。

* **PiCO: Contrastive Label Disambiguation for Partial Label Learning**
  [论文](https://openreview.net/forum?id=EhYjZy6e1gJ) · Haobo Wang, Ruixuan Xiao, Yixuan Li, Lei Feng, Gang Niu, Gang Chen, Junbo Zhao
  用对比学习和原型一起做标签消歧，把表示学习和消歧放进同一个框架。

## 时间检验奖

原论文早于 2022，是后来的会议回看约十年前的工作。不放进上面各年的研究地图。

* **Unsupervised Representation Learning with Deep Convolutional Generative Adversarial Networks**（Test of Time，2026 年颁发，原论文 2016）
  [论文](https://arxiv.org/abs/1511.06434) · Alec Radford, Luke Metz, Soumith Chintala
  DCGAN 证明卷积 GAN 可以合成多样、看起来真实的图像。

* **Continuous control with deep reinforcement learning**（Test of Time，2026 年颁发，原论文 2016）
  [论文](https://arxiv.org/abs/1509.02971) · Timothy P. Lillicrap, Jonathan J. Hunt, Alexander Pritzel, Nicolas Heess, Tom Erez, Yuval Tassa, David Silver, Daan Wierstra
  提出 DDPG，把确定性演员-评论家和 DQN 的稳定技巧合在一起，直接输出连续动作。

* **Adam: A Method for Stochastic Optimization**（Test of Time，2025 年颁发，原论文 2015）
  [论文](https://arxiv.org/abs/1412.6980) · Diederik P. Kingma, Jimmy Ba
  提出结合一阶矩和二阶矩的自适应随机优化方法 Adam。

* **Neural Machine Translation by Jointly Learning to Align and Translate**（Test of Time Runner-up，2025 年颁发，原论文 2015）
  [论文](https://arxiv.org/abs/1409.0473) · Dzmitry Bahdanau, Kyunghyun Cho, Yoshua Bengio
  在神经机器翻译里联合学习对齐和翻译，引入加性注意力。

* **Auto-Encoding Variational Bayes**（Test of Time，2024 年颁发，原论文 2014）
  [论文](https://arxiv.org/abs/1312.6114) · Diederik P. Kingma, Max Welling
  提出用重参数化梯度训练变分自编码器。

* **Intriguing properties of neural networks**（Test of Time Runner-up，2024 年颁发，原论文 2014）
  [论文](https://arxiv.org/abs/1312.6199) · Christian Szegedy, Wojciech Zaremba, Ilya Sutskever, Joan Bruna, Dumitru Erhan, Ian Goodfellow, Rob Fergus
  展示深度网络对微小扰动会给出高置信的错误预测。

# NeurIPS

## 2026

待补充。会议于 2026 年 12 月 6–12 日在悉尼举行，官方博客在 11 月 25 日之前只公布了教程、期刊轨道和可重复性轨道，没有公布 Best Paper。

## 2025

### Best Paper

* **Artificial Hivemind: The Open-Ended Homogeneity of Language Models (and Beyond)**
  [论文](https://arxiv.org/abs/2510.22954) · Liwei Jiang, Yuanjun Chai, Margaret Li, Mickel Liu, Raymond Fok, Nouha Dziri 等
  用开放式真实提问组成的 Infinity-Chat 研究模型内部和模型之间的回答同质化。

* **Gated Attention for Large Language Models: Non-linearity, Sparsity, and Attention-Sink-Free**
  [论文](https://arxiv.org/abs/2505.06708) · Zihan Qiu, Zekun Wang, Bo Zheng, Zeyu Huang, Kaiyue Wen, Songlin Yang 等
  系统比较给 softmax 注意力加门控的方式，看非线性、稀疏和注意力汇聚分别从哪来。

* **1000 Layer Networks for Self-Supervised RL: Scaling Depth Can Enable New Goal-Reaching Capabilities**
  [论文](https://arxiv.org/abs/2503.14858) · Kevin Wang, Ishaan Javali, Michał Bortkiewicz, Tomasz Trzcinski, Benjamin Eysenbach
  把自监督强化学习网络做到很深，观察深度本身会带来新的目标到达能力。

* **Why Diffusion Models Don’t Memorize: The Role of Implicit Dynamical Regularization in Training**
  [论文](https://arxiv.org/abs/2505.17638) · Tony Bonnaire, Raphaël Urfin, Giulio Biroli, Marc Mézard
  从训练动力学里的隐式正则解释扩散模型为什么常常不直接记住训练集。

### Best Paper Runner-up

* **Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model?**
  [论文](https://arxiv.org/abs/2504.13837) · Yang Yue, Zhiqi Chen, Rui Lu, Andrew Zhao, Zhaokai Wang, Shiji Song, Gao Huang
  检查强化学习后训练究竟是让基座模型获得了新的推理能力，还是把已有能力抽取得更频繁。

* **Optimal Mistake Bounds for Transductive Online Learning**
  [论文](https://openreview.net/forum?id=EoebmBe9fG) · Zachary Chase, Steve Hanneke, Shay Moran, Jonathan Shafer
  解决直推在线学习里一个约三十年的失误界问题。

* **Superposition Yields Robust Neural Scaling**
  [论文](https://arxiv.org/abs/2505.10465) · Yizhou Liu, Ziming Liu, Jeff Gore
  用叠加表示解释神经缩放为何对架构和噪声相对稳健。

## 2024

### Best Paper

* **Visual Autoregressive Modeling: Scalable Image Generation via Next-Scale Prediction**
  [论文](https://openreview.net/forum?id=gojL67CfS8) · Keyu Tian, Yi Jiang, Zehuan Yuan, Bingyue Peng, Liwei Wang
  用下一尺度预测代替下一图块预测，让图像自回归按分辨率从粗到细生成。

* **Stochastic Taylor Derivative Estimator: Efficient amortization for arbitrary differential operators**
  [论文](https://openreview.net/forum?id=J2wI2rCG2u) · Zekun Shi, Zheyuan Hu, Min Lin, Kenji Kawaguchi
  用随机泰勒展开估计任意阶微分算子，使高阶、高维的物理信息网络训练变得可算。

### Best Paper Runner-up

* **Not All Tokens Are What You Need for Pretraining**
  [论文](https://openreview.net/forum?id=0NMzBwqaAJ) · Zhenghao Lin, Zhibin Gou, Yeyun Gong, Xiao Liu, Yelong Shen, Ruochen Xu 等
  用一个在高质量参考集上训过的模型给大语料的 token 打分，只留下排序靠前的 token 做正式预训练。

* **Guiding a Diffusion Model with a Bad Version of Itself**
  [论文](https://openreview.net/forum?id=bg6fVPVs3s) · Tero Karras, Miika Aittala, Tuomas Kynkäänniemi, Jaakko Lehtinen, Timo Aila, Samuli Laine
  用一个更差、更噪的同类模型代替无条件分支来做引导，以缓解无分类器引导损失多样性的问题。

### Best Paper, Datasets and Benchmarks

* **The PRISM Alignment Dataset: What Participatory, Representative and Individualised Human Feedback Reveals About the Subjective and Multicultural Alignment of Large Language Models**
  [论文](https://openreview.net/forum?id=DFr5hteojx) · Hannah Rose Kirk, Alexander Whitefield, Paul Röttger, Andrew Bean, Katerina Margatina, Juan Ciro 等
  收集来自多个国家、允许主观和多元偏好的人类反馈，用来研究对齐不该被收成单一奖励。

## 2023

### Outstanding Paper

* **Privacy Auditing with One (1) Training Run**
  [论文](https://arxiv.org/abs/2305.08846) · Thomas Steinke, Milad Nasr, Matthew Jagielski
  用一次训练同时加入或去掉多个样本，给差分隐私系统做出经验下界，而不必训练上百个模型。

* **Are Emergent Abilities of Large Language Models a Mirage?**
  [论文](https://arxiv.org/abs/2304.15004) · Rylan Schaeffer, Brando Miranda, Sanmi Koyejo
  指出所谓涌现能力往往来自不连续的评测指标，换成分数平滑的指标后，性能随规模是连续变化的。

### Outstanding Paper Runner-up

* **Scaling Data-Constrained Language Models**
  [论文](https://arxiv.org/abs/2305.16264) · Niklas Muennighoff, Alexander Rush, Boaz Barak, Teven Le Scao, Nouamane Tazi, Aleksandra Piktus 等
  在数据不够独特时研究重复训练，发现少量重复几乎不伤损失，重复太多则多加的算力会失效。

* **Direct Preference Optimization: Your Language Model is Secretly a Reward Model**
  [论文](https://arxiv.org/abs/2305.18290) · Rafael Rafailov, Archit Sharma, Eric Mitchell, Christopher D. Manning, Stefano Ermon, Chelsea Finn
  证明带 KL 约束的偏好优化可以化成一次分类式微调，从而不必单独训练奖励模型再跑强化学习。

### Outstanding Datasets and Benchmarks Paper

* **ClimSim: A large multi-scale dataset for hybrid physics-ML climate emulation**
  [论文](https://arxiv.org/abs/2306.08754) · Sungduk Yu, Walter Hannah, Liran Peng, Jerry Lin, Mohamed Aziz Bhouri 等
  发布面向物理与机器学习混合模拟的多尺度气候数据，使高分辨率物理过程可以被学习器仿真。

* **DecodingTrust: A Comprehensive Assessment of Trustworthiness in GPT Models**
  [论文](https://arxiv.org/abs/2306.11698) · Boxin Wang, Weixin Chen, Hengzhi Pei, Chulin Xie, Mintong Kang, Chenhui Zhang 等
  从毒性、偏见、对抗、隐私、伦理和公平等多个面评估 GPT 模型的可信度。

## 2022

### Outstanding Paper

* **Is Out-of-distribution Detection Learnable?**
  [论文](https://openreview.net/forum?id=sde_7ZzGXOE) · Zhen Fang, Yixuan Li, Jie Lu, Jiahua Dong, Bo Han, Feng Liu
  用 PAC 学习刻画分布外检测在什么分布族和模型族下可学，并给出几条不可学定理。

* **Photorealistic Text-to-Image Diffusion Models with Deep Language Understanding**
  [论文](https://openreview.net/forum?id=08Yk-n5l2Al) · Chitwan Saharia, William Chan, Saurabh Saxena, Lala Li, Jay Whang, Emily Denton 等
  把单独训练的大语言模型和图像扩散解码器接在一起，做出高保真的文本生成图像模型 Imagen。

* **Elucidating the Design Space of Diffusion-Based Generative Models**
  [论文](https://openreview.net/forum?id=k7FuTOWMOc7) · Tero Karras, Miika Aittala, Timo Aila, Samuli Laine
  把已有扩散模型收成同一套设计空间，指出采样、预条件和训练目标里哪些选择真正起作用。

* **ProcTHOR: Large-Scale Embodied AI Using Procedural Generation**
  [论文](https://openreview.net/forum?id=4-bV1bi74M) · Matt Deitke, Eli VanderBilt, Alvaro Herrasti, Luca Weihs, Kiana Ehsani, Jordi Salvador 等
  用程序化生成做出可交互的大规模室内环境，让具身智能体也能吃到数据规模。

* **Using natural language and program abstractions to instill human inductive biases in machines**
  [论文](https://openreview.net/forum?id=buXZ7nIqiwE) · Sreejan Kumar, Carlos G. Correa, Ishita Dasgupta, Raja Marjieh, Michael Hu, Robert D. Hawkins 等
  让模型同时在自然语言和程序抽象上训练，从而带上人在解决任务时用的那种偏置。

* **A Neural Corpus Indexer for Document Retrieval**
  [论文](https://openreview.net/forum?id=fSfcEYQP_qc) · Yujing Wang, Yingyan Hou, Haonan Wang, Ziming Miao, Shibin Wu, Hao Sun 等
  训练一个解码器，让查询直接生成文档标识，而不是先做稀疏召回再重排。

* **High-dimensional limit theorems for SGD: Effective dynamics and critical scaling**
  [论文](https://openreview.net/forum?id=Q38D6xxrKHe) · Gerard Ben Arous, Reza Gheissari, Aukosh Jagannath
  给出高维、固定步长 SGD 的极限定理，说明步长大时有效动力学会从 ODE 变成更复杂的随机方程。

* **Gradient Descent: The Ultimate Optimizer**
  [论文](https://openreview.net/forum?id=-Qp-3L-5ZdI) · Kartik Chandra, Audrey Xie, Jonathan Ragan-Kelley, Erik Meijer
  把超参也交给梯度下降，并允许对超超参继续自动求导。

* **Riemannian Score-Based Generative Modelling**
  [论文](https://openreview.net/forum?id=oDRQGo8I7P) · Valentin De Bortoli, Emile Mathieu, Michael Hutchinson, James Thornton, Yee Whye Teh, Arnaud Doucet
  把 score-based 生成从欧氏空间推广到黎曼流形，并指出哪些部件是成功所依赖的。

* **Gradient Estimation with Discrete Stein Operators**
  [论文](https://openreview.net/forum?id=I1mkUkaguP) · Jiaxin Shi, Yuhao Zhou, Jessica Hwang, Michalis Titsias, Lester Mackey
  用离散 Stein 算子给离散分布的梯度估计做方差缩减。

* **An empirical analysis of compute-optimal large language model training**
  [论文](https://openreview.net/forum?id=iBBcRUlOAPR) · Jordan Hoffmann, Sebastian Borgeaud, Arthur Mensch, Elena Buchatskaya, Trevor Cai, Eliza Rutherford 等
  在固定算力下重新权衡模型大小和训练 token 数，得出更小的模型配更多数据可以更优，即 Chinchilla。

* **Beyond neural scaling laws: beating power law scaling via data pruning**
  [论文](https://openreview.net/forum?id=UmvSlP-PyV) · Ben Sorscher, Robert Geirhos, Shashank Shekhar, Surya Ganguli, Ari S. Morcos
  用理论和 ImageNet 上的筛选实验说明，丢掉低质量数据可以打穿幂律缩放。

* **On-Demand Sampling: Learning Optimally from Multiple Distributions**
  [论文](https://openreview.net/forum?id=FR289LMkmxZ) · Nika Haghtalab, Michael I. Jordan, Eric Zhao
  用零和博弈的技术做按需采样，在多个分布上学习时接近最优地分配样本。

### Outstanding Datasets and Benchmarks Paper

* **LAION-5B: An open large-scale dataset for training next generation image-text models**
  [论文](https://openreview.net/forum?id=M3Y74vmsMcY) · Christoph Schuhmann, Romain Beaumont, Richard Vencu, Cade Gordon, Ross Wightman, Mehdi Cherti 等
  公开约 58 亿条经过 CLIP 过滤的图文对，并用来复现 CLIP、GLIDE 和 Stable Diffusion 一类模型。

* **MineDojo: Building Open-Ended Embodied Agents with Internet-Scale Knowledge**
  [论文](https://openreview.net/forum?id=rc8o_j8I8PX) · Linxi Fan, Guanzhi Wang, Yunfan Jiang, Ajay Mandlekar, Yuncong Yang, Haoyi Zhu 等
  在 Minecraft 上提供大量开放任务，外加视频、教程和维基组成的互联网规模知识，用来训练语言指定的开放智能体。

## 时间检验奖

原论文早于 2022，是后来的会议回看约十年前的工作。不放进上面各年的研究地图。

* **Faster R-CNN: Towards Real-Time Object Detection with Region Proposal Networks**（Test of Time，2025 年颁发，原论文 2015）
  [论文](https://arxiv.org/abs/1506.01497) · Shaoqing Ren, Kaiming He, Ross Girshick, Jian Sun
  把区域提议也做成卷积网络，使检测可以接近实时地端到端训练。

* **Generative Adversarial Nets**（Test of Time，2024 年颁发，原论文 2014）
  [论文](https://arxiv.org/abs/1406.2661) · Ian Goodfellow, Jean Pouget-Abadie, Mehdi Mirza, Bing Xu, David Warde-Farley, Sherjil Ozair, Aaron Courville, Yoshua Bengio
  提出用生成器和判别器对抗训练来学习生成分布。

* **Sequence to Sequence Learning with Neural Networks**（Test of Time，2024 年颁发，原论文 2014）
  [论文](https://arxiv.org/abs/1409.3215) · Ilya Sutskever, Oriol Vinyals, Quoc V. Le
  用编码器-解码器网络做序列到序列学习，并在机器翻译上展示深度 LSTM 的效果。

* **Distributed Representations of Words and Phrases and their Compositionality**（Test of Time，2023 年颁发，原论文 2013）
  [论文](https://papers.nips.cc/paper_files/paper/2013/hash/9aa42b31882ec039965f3c4923ce901b-Abstract.html) · Tomas Mikolov, Ilya Sutskever, Kai Chen, Greg Corrado, Jeffrey Dean
  word2vec 用大规模无结构文本学习词和短语的分布式表示。

* **ImageNet Classification with Deep Convolutional Neural Networks**（Test of Time，2022 年颁发，原论文 2012）
  [论文](https://papers.nips.cc/paper/2012/file/c399862d3b9d6b76c8436e924a68c45b-Paper.pdf) · Alex Krizhevsky, Ilya Sutskever, Geoffrey E. Hinton
  AlexNet 用深度卷积网络在 ImageNet 上大幅超过当时的视觉系统。

# ICML

## 2026

### Outstanding Paper

* **The Flexibility Trap: Rethinking the Value of Arbitrary Order in Diffusion Language Models**
  [论文](https://arxiv.org/abs/2601.15165) · Zanlin Ni, Shenzhi Wang, Yang Yue, Tianyu Yu, Weilin Zhao, Yeguo Hua 等
  指出扩散语言模型在一般推理上会利用任意顺序绕开高不确定的分叉 token，从而损失解的多样性；建议强化学习仍按从左到右采样。

* **High-Accuracy Sampling for Diffusion Models and Log-Concave Distributions**
  [论文](https://arxiv.org/abs/2602.01338) · Fan Chen, Sinho Chewi, Constantinos Daskalakis, Alexander Rakhlin
  证明在分数估计足够准时，扩散采样可以用相对误差只呈多对数的步数达到高精度，并给出只靠梯度的对数凹采样。

### Outstanding Paper Honorable Mention

* **The Obfuscation Atlas: Mapping Where Honesty Emerges in RLVR with Deception Probes**
  [论文](https://arxiv.org/abs/2602.15515) · Mohammad Taufeeque, Stefan Heimersheim, Adam Gleave, Chris Cundy
  在会奖励黑客的代码优化环境里，用欺骗探针追踪强化学习怎样绕过诚实检测，并区分明目张胆的欺骗和把激活或策略藏起来。

* **Motion Attribution for Video Generation**
  [论文](https://arxiv.org/abs/2601.08828) · Xindi Wu, Despoina Paschalidou, Jun Gao, Antonio Torralba, Laura Leal-Taixé, Olga Russakovsky, Sanja Fidler, Jonathan Lorraine
  追踪每条训练视频对测试运动质量的贡献，从而用少得多的数据提升运动。

* **How much can language models memorize?**
  [论文](https://arxiv.org/abs/2505.24832) · John X. Morris, Chawin Sitawarin, Narine Kokhlikyan, Chuan Guo, G. Edward Suh, Alexander M. Rush, Kamalika Chaudhuri, Saeed Mahloujifar
  用可计算的记忆定义区分模型有意记住的分布结构和无意记住的训练细节。

* **A Random Matrix Perspective on the Consistency of Diffusion Models**
  [论文](https://arxiv.org/abs/2602.02908) · Binxu Wang, Jacob A. Zavatone-Veth, Cengiz Pehlevan
  用随机矩阵解释不同训练划分、不同架构的扩散模型为什么会把同一个噪声种子映到几乎相同的图像。

* **To Grok Grokking: Provable Grokking in Ridge Regression**
  [论文](https://arxiv.org/abs/2601.19791) · Mingyue Xu, Gal Vardi, Itay Safran
  在岭回归这个线性模型里证明两阶段的顿悟现象：先拟合后泛化。

### Outstanding Position Paper Honorable Mention

* **Position: AI/ML Deepfake Research is Misaligned with AI Generated Non-Consensual Intimate Imagery (AIG-NCII)**
  [论文](https://arxiv.org/abs/2607.18263) · Li Qiwei, Wells Lucas Santo, Sarita Schoenebeck, Eric Gilbert
  指出深度伪造检测研究的任务设置和未经同意的亲密影像这一真实伤害并不对齐。

### Outstanding Position Paper

* **Position: The Alignment Community is Unintentionally Building a Censor’s Toolkit**
  [论文](https://arxiv.org/abs/2608.12346) · Sarah Ball, Phil Hackemann
  指出价值对齐的工具同样可以被权威用来审查，并用现实证据说明这不是个别国家的问题。

## 2025

### Outstanding Paper

* **CollabLLM: From Passive Responders to Active Collaborators**
  [论文](https://arxiv.org/abs/2502.00640) · Shirley Wu, Michel Galley, Baolin Peng, Hao Cheng, Gavin Li, Yao Dou 等
  用多轮仿真估计一条回复的长期贡献，再以此做强化学习，让模型主动澄清而不是被动作答。

* **Train for the Worst, Plan for the Best: Understanding Token Ordering in Masked Diffusions**
  [论文](https://arxiv.org/abs/2502.06768) · Jaeyeon Kim, Kulin Shah, Vasilis Kontonis, Sham Kakade, Sitan Chen
  分析掩码扩散在训练时要面对的填空难度，以及推理时自适应决定解开哪个 token 能绕开难题。

* **Score Matching with Missing Data**
  [论文](https://arxiv.org/abs/2506.00557) · Josh Givens, Song Liu, Henry Reeve
  把得分匹配推广到任意坐标子集缺失的数据，并给出重要性加权和变分两种做法。

* **Conformal Prediction as Bayesian Quadrature**
  [论文](https://arxiv.org/abs/2502.13228) · Jake Snell, Thomas Griffiths
  从贝叶斯数值积分重新看共形预测，说明频率保证之外还可以给出损失范围的更丰富表示。

* **Roll the dice & look before you leap: Going beyond the creative limits of next-token prediction**
  [论文](https://arxiv.org/abs/2504.15266) · Vaishnavh Nagarajan, Chen Wu, Charles Ding, Aditi Raghunathan
  用一组最小的算法任务说明下一 token 预测在需要远见的开放式任务上短视，多 token 目标更有创造性。

* **The Value of Prediction in Identifying the Worst-Off**
  [论文](https://arxiv.org/abs/2501.19334) · Unai Fischer-Abaigar, Christoph Kern, Juan Perdomo
  比较用预测去找出最困难的人，和扩大行政能力等其他政策杠杆，哪一种更改善福利。

### Outstanding Position Paper

* **Position: The AI Conference Peer Review Crisis Demands Author Feedback and Reviewer Rewards**
  [论文](https://arxiv.org/abs/2505.04966) · Jaeho Kim, Yunseok Lee, Seulki Lee
  主张把单向审稿改成作者可以评价审稿、审稿人获得正式信用的双向机制。

* **Position: AI Safety should prioritize the Future of Work**
  [论文](https://arxiv.org/abs/2504.13959) · Sanchaita Hazra, Bodhisattwa Prasad Majumder, Tuhin Chakrabarty
  主张人工智能安全不该只看有害内容和极端风险，还要把劳动、收入分配和人的能动性放进安全议程。

## 2024

### Best Paper

* **VideoPoet: A Large Language Model for Zero-Shot Video Generation**
  [论文](https://arxiv.org/abs/2312.14125) · Dan Kondratyuk, Lijun Yu, Xiuye Gu, Jose Lezama, Jonathan Huang, Lu Jiang 等
  用解码器式语言模型吃进图像、视频、文本和音频，再零样本生成视频。

* **Debating with More Persuasive LLMs Leads to More Truthful Answers**
  [论文](https://arxiv.org/abs/2402.06782) · Akbir Khan, John Hughes, Dan Valentine, Laura Ruis, Kshitij Sachan, Ansh Radhakrishnan 等
  让更会说服的模型参与辩论，观察这是否让最终答案更接近真相。

* **Genie: Generative Interactive Environments**
  [论文](https://arxiv.org/abs/2402.15391) · Jake Bruce, Michael Dennis, Ashley Edwards, Jack Parker-Holder, Tim Rocktäschel 等
  从无动作标签的互联网视频学习可交互的生成环境，用户可以逐帧采取动作。

* **Position: Measure Dataset Diversity, Don't Just Claim It**
  [论文](https://arxiv.org/abs/2407.08188) · Dora Zhao, Jerone Andrews, Orestis Papakyriakopoulos, Alice Xiang
  检查一百多个数据集如何使用多样性这个词，要求按测量理论去操作化，而不是只在摘要里声称。

* **Stealing part of a production language model**
  [论文](https://arxiv.org/abs/2403.06634) · Nicholas Carlini, Daniel Paleka, Krishnamurthy Dvijotham, Thomas Steinke, Jonathan Hayase, A. Feder Cooper 等
  通过普通 API 查询恢复生产语言模型的嵌入投影矩阵，从而得知隐藏维度等结构信息。

* **Scaling Rectified Flow Transformers for High-Resolution Image Synthesis**
  [论文](https://arxiv.org/abs/2403.03206) · Patrick Esser, Sumith Kulal, Andreas Blattmann, Rahim Entezari, Jonas Müller, Harry Saini 等
  把整流流和 Transformer 骨干放大到高分辨率文生图，即 Stable Diffusion 3 的技术路线。

* **Position: Considerations for Differentially Private Learning with Large-Scale Public Pretraining**
  [论文](https://arxiv.org/abs/2212.06470) · Florian Tramèr, Gautam Kamath, Nicholas Carlini
  质疑在大规模公开预训练之上做差分隐私微调时，公开数据真的算公开、基准又是否测到了敏感域。

* **Information Complexity of Stochastic Convex Optimization: Applications to Generalization, Memorization, and Tracing**
  [论文](https://arxiv.org/abs/2402.09327) · Idan Attias, Gintare Karolina Dziugaite, Mahdi Haghifam, Roi Livni, Daniel Roy
  用信息复杂度统一地讨论随机凸优化里的泛化、记忆和训练数据追踪。

* **Probabilistic Inference in Language Models via Twisted Sequential Monte Carlo**
  [论文](https://arxiv.org/abs/2404.17546) · Stephen Zhao, Rob Brekelmans, Alireza Makhzani, Roger Grosse
  用带 twist 的序贯蒙特卡洛，从由奖励定义的非归一化分布里给语言模型抽样。

* **Discrete Diffusion Modeling by Estimating the Ratios of the Data Distribution**
  [论文](https://arxiv.org/abs/2310.16834) · Aaron Lou, Chenlin Meng, Stefano Ermon
  通过估计数据分布的比值来做离散扩散，避开直接建模高维离散分数的困难。

## 2023

### Outstanding Paper

* **Learning-Rate-Free Learning by D-Adaptation**
  [论文](https://openreview.net/forum?id=GXZ6cT5cvY) · Aaron Defazio, Konstantin Mishchenko
  提出不需要设定学习率的 D-Adaptation，用距离估计自动放大步长。

* **A Watermark for Large Language Models**
  [论文](https://openreview.net/forum?id=aX8ig9X2a7) · John Kirchenbauer, Jonas Geiping, Yuxin Wen, Jonathan Katz, Ian Miers, Tom Goldstein
  在解码时偏向一组绿名单 token，从而给语言模型输出打上可检测的水印。

* **Generalization on the Unseen, Logic Reasoning and Degree Curriculum**
  [论文](https://openreview.net/forum?id=3dqwXb1te4) · Emmanuel Abbe, Samy Bengio, Aryo Lotfi, Kevin Rizk
  研究网络在没见过的逻辑难度上如何泛化，并用度数课程解释什么样的训练顺序能走得更远。

* **Adapting to game trees in zero-sum imperfect information games**
  [论文](https://openreview.net/forum?id=O1j4uFuSVW) · Côme Fiegel, Pierre Ménard, Tadashi Kozuno, Rémi Munos, Vianney Perchet, Michal Valko
  给零和不完全信息博弈一个能适应具体博弈树结构的算法，而不是只依赖最坏情况界。

* **Self-Repellent Random Walks on General Graphs - Achieving Minimal Sampling Variance via Nonlinear Markov Chains**
  [论文](https://openreview.net/forum?id=450iImFM4U) · Vishwaraj Doshi, Jie Hu, Do Young Eun
  用非线性马尔可夫链构造自我排斥的随机游走，使一般图上的采样方差接近最小。

* **Bayesian Design Principles for Frequentist Sequential Learning**
  [论文](https://openreview.net/forum?id=tRhQsHnoFw) · Yunbei Xu, Assaf Zeevi
  用贝叶斯设计原则去构造有频率学派保证的序贯学习算法。

## 2022

### Outstanding Paper

* **Do Differentiable Simulators Give Better Policy Gradients?**
  [论文](https://arxiv.org/abs/2202.00817) · Hyung Ju Suh, Max Simchowitz, Kaiqing Zhang, Russ Tedrake
  分析可微模拟器给出的策略梯度在什么时候比打分函数估计更好，什么时候会因为接触和不连续而变差。

* **Causal Conceptions of Fairness and their Consequences**
  [论文](https://arxiv.org/abs/2207.05302) · Hamed Nilforoshan, Johann Gaebler, Ravi Shroff, Sharad Goel
  考察把公平写成因果量之后，决策会带来什么后果，包括和常见公平准则的冲突。

* **G-Mixup: Graph Data Augmentation for Graph Classification**
  [论文](https://arxiv.org/abs/2202.07179) · Xiaotian Han, Zhimeng Jiang, Ninghao Liu, Xia Hu
  在图分类里对图的表示做 mixup 式增广，而不是在原始邻接矩阵上硬插值。

* **Stable Conformal Prediction Sets**
  [论文](https://arxiv.org/abs/2112.10224) · Eugene Ndiaye
  研究预测集合对训练数据扰动的稳定性，避免共形集合因为换一个样本就剧烈变化。

* **Privacy for Free: How does Dataset Condensation Help Privacy?**
  [论文](https://arxiv.org/abs/2206.00240) · Tian Dong, Bo Zhao, Lingjuan Lyu
  分析把训练集蒸馏成少量合成样本之后，对成员隐私会有什么影响。

* **Solving Stackelberg Prediction Game with Least Squares Loss via Spherically Constrained Least Squares Reformulation**
  [论文](https://arxiv.org/abs/2206.02991) · Jiali Wang, Wen Huang, Rujun Jiang, Xudong Li, Alex L. Wang
  把最小二乘损失下的 Stackelberg 预测博弈改写成球面约束最小二乘，从而能解。

* **The Importance of Non-Markovianity in Maximum State Entropy Exploration**
  [论文](https://arxiv.org/abs/2202.03060) · Mirco Mutti, Riccardo De Santi, Marcello Restelli
  说明最大状态熵探索如果只看马尔可夫策略，会错过必须依赖历史的探索行为。

* **Bayesian Model Selection, the Marginal Likelihood, and Generalization**
  [论文](https://arxiv.org/abs/2202.11678) · Sanae Lotfi, Pavel Izmailov, Gregory Benton, Micah Goldblum, Andrew Gordon Wilson
  重新检查边际似然作为模型选择准则时，和泛化之间到底是什么关系。

* **Understanding Dataset Difficulty with V-Usable Information**
  [论文](https://arxiv.org/abs/2110.08420) · Kawin Ethayarajh, Yejin Choi, Swabha Swayamdipta
  用 V-information 衡量一个数据集对给定模型家族到底还剩多少可用信息。

* **Learning Mixtures of Linear Dynamical Systems**
  [论文](https://arxiv.org/abs/2201.11211) · Yanxi Chen, H. Vincent Poor
  研究如何从轨迹里学习线性动力系统的混合，而不是假设全世界只有一个线性系统。

### Outstanding Paper Runner-up

* **Active fairness auditing**
  [论文](https://arxiv.org/abs/2206.08450) · Tom Yan, Chicheng Zhang
  主动选择要查询的样本来审计一个模型是否公平，而不是被动地看一批固定数据。

* **Adversarially Trained Actor Critic for Offline Reinforcement Learning**
  [论文](https://arxiv.org/abs/2202.02446) · Ching-An Cheng, Tengyang Xie, Nan Jiang, Alekh Agarwal
  用对抗训练稳定离线演员-评论家，减轻分布外动作把价值估计带偏。

* **Monarch: Expressive Structured Matrices for Efficient and Accurate Training**
  [论文](https://arxiv.org/abs/2204.00595) · Tri Dao, Beidi Chen, Nimit S. Sohoni, Arjun D. Desai, Michael Poli, Jessica Grogan 等
  用 Monarch 矩阵这种结构化矩阵替换稠密层，在表达力和计算成本之间取一个可训练的中间点。

* **Learning inverse folding from millions of predicted structures**
  [论文](https://doi.org/10.1101/2022.04.10.487779) · Chloe Hsu, Robert Verkuil, Jason Liu, Zeming Lin, Brian Hie, Tom Sercu, Adam Lerer, Alexander Rives
  用数百万预测结构训练逆向折叠模型，从结构找回会折叠成它的序列。

* **Minimum Cost Intervention Design for Causal Effect Identification**
  [论文](https://proceedings.mlr.press/v162/akbari22a.html) · Sina Akbari, Jalal Etesami, Negar Kiyavash
  在要识别因果效应时，设计代价最小的一组干预。

## 时间检验奖

原论文早于 2022，是后来的会议回看约十年前的工作。不放进上面各年的研究地图。

* **Asynchronous Methods for Deep Reinforcement Learning**（Test of Time，2026 年颁发，原论文 2016）
  [论文](https://arxiv.org/abs/1602.01783) · Volodymyr Mnih, Adrià Puigdomènech Badia, Mehdi Mirza, Alex Graves, Timothy P. Lillicrap, Tim Harley, David Silver, Koray Kavukcuoglu
  提出异步优势演员-评论家等方法，用并行的演员稳定深度强化学习。

* **Batch Normalization: Accelerating Deep Network Training by Reducing Internal Covariate Shift**（Test of Time，2025 年颁发，原论文 2015）
  [论文](https://arxiv.org/abs/1502.03167) · Sergey Ioffe, Christian Szegedy
  提出批量归一化，把每层输入拉回稳定的尺度，从而允许更大的学习率。

* **Trust Region Policy Optimization**（Test of Time Honorable Mention，2025 年颁发，原论文 2015）
  [论文](https://arxiv.org/abs/1502.05477) · John Schulman, Sergey Levine, Pieter Abbeel, Michael I. Jordan, Philipp Moritz
  提出信赖域策略优化，在保证策略改进更可控的约束下更新大神经网络策略。

* **Variational Inference with Normalizing Flows**（Test of Time Honorable Mention，2025 年颁发，原论文 2015）
  [论文](https://arxiv.org/abs/1505.05770) · Danilo Jimenez Rezende, Shakir Mohamed
  用可逆变换把简单分布逐步变成复杂近似后验，即归一化流。

* **DeCAF: A Deep Convolutional Activation Feature for Generic Visual Recognition**（Test of Time，2024 年颁发，原论文 2014）
  [论文](https://arxiv.org/abs/1310.1531) · Jeff Donahue, Yangqing Jia, Oriol Vinyals, Judy Hoffman, Ning Zhang, Eric Tzeng, Trevor Darrell
  把在大分类任务上训练的卷积网络激活当成通用视觉特征，迁移到场景、细粒度和域适应。

* **Learning Fair Representations**（Test of Time，2023 年颁发，原论文 2013）
  [论文](https://proceedings.mlr.press/v28/zemel13.html) · Richard Zemel, Yu Wu, Kevin Swersky, Toni Pitassi, Cynthia Dwork
  学习一种既保留任务信息、又让敏感属性难以被读出的表示。

* **Deep Canonical Correlation Analysis**（Test of Time Runner-up，2023 年颁发，原论文 2013）
  [论文](https://proceedings.mlr.press/v28/andrew13.html) · Galen Andrew, Raman Arora, Jeff Bilmes, Karen Livescu
  把典型相关分析做到深度网络，让两种视图的表示按相关而不是按重构对齐。

* **Making a Science of Model Search: Hyperparameter Optimization in Hundreds of Dimensions for Vision Architectures**（Test of Time Runner-up，2023 年颁发，原论文 2013）
  [论文](https://proceedings.mlr.press/v28/bergstra13.html) · James Bergstra, Daniel Yamins, David Cox
  把超参搜索写成可以比较的实验科学，而不是每个人一套手调。

* **Poisoning Attacks Against Support Vector Machines**（Test of Time，2022 年颁发，原论文 2012）
  [论文](https://arxiv.org/abs/1206.6389) · Battista Biggio, Blaine Nelson, Pavel Laskov
  展示通过污染训练集可以操纵支持向量机的预测。

* **Building high-level features using large scale unsupervised learning**（Test of Time Honorable Mention，2022 年颁发，原论文 2012）
  [论文](https://arxiv.org/abs/1112.6209) · Quoc V. Le, Marc'Aurelio Ranzato, Rajat Monga, Matthieu Devin, Kai Chen, Greg S. Corrado, Jeff Dean, Andrew Y. Ng
  用大规模无监督训练从图像里学出高层特征，包括对高层概念有选择性的单元。

* **On causal and anticausal learning**（Test of Time Honorable Mention，2022 年颁发，原论文 2012）
  [论文](https://arxiv.org/abs/1206.6471) · Bernhard Schölkopf, Dominik Janzing, Jonas Peters, Eleni Sgouritsa, Kun Zhang, Joris M. Mooij
  区分因果方向和反因果方向上的学习问题，说明预测和干预不该混用同一套假设。

# ACL

## 2026

### Best Paper

* **The Imperfective Paradox in Large Language Models**
  [论文](https://aclanthology.org/2026.acl-long.689) · Bolei Ma, Yusuke Miyao
  未完成体悖论是语言学里的老问题；这篇看大模型会不会在体貌上犯和人不一样的错。

* **Memory Efficiency and Resource-Rational Encoding in Sentence Processing**
  [论文](https://aclanthology.org/2026.acl-long.1550) · Weijie Xu, Brian Dillon, Richard Futrell
  句子加工的记忆效率可以写成资源理性的编码问题，模型和人类的限制放在同一把尺子上。

* **Characterizing the Expressivity of Local Attention in Transformers**
  [论文](https://aclanthology.org/2026.acl-long.1739) · Jiaoda Li, Ryan Cotterell
  局部注意力的表达力需要单独刻画，不能用全注意力的结论直接套。

### Outstanding Paper

* **MauBERT: Universal Phonetic Inductive Biases for Few-Shot Acoustic Units Discovery**
  [论文](https://aclanthology.org/2026.acl-long.24) · Angelo Ortiz Tandazo, Manel Khentout, Youssef Benchekroun, Thomas Hueber, Emmanuel Dupoux

* **Evolutionary Guided Decoding: Iterative Value Refinement for LLMs**
  [论文](https://aclanthology.org/2026.acl-long.148) · Zhenhua Liu, Lijun Li, Ruizhe Chen, Yuxian Jiang, Tong Zhu, Zhaochen Su, Wenliang Chen, Jing Shao

* **Beyond the Final Actor: Modeling the Dual Roles of Creator and Editor for Fine-Grained LLM-Generated Text Detection**
  [论文](https://aclanthology.org/2026.acl-long.235) · Yang Li, Qiang Sheng, Zhengjia Wang, Yehan Yang, Danding Wang, Juan Cao

* **Lying with Truths: Open-Channel Multi-Agent Collusion for Belief Manipulation via Generative Montage**
  [论文](https://aclanthology.org/2026.acl-long.270) · Jinwei Hu, Xinmiao Huang, Youcheng Sun, Yi Dong, Xiaowei Huang

* **Hierarchical Acoustic-Semantic Modeling: Modality Separation and Semantic Coherence for Full-Duplex SLMs**
  [论文](https://aclanthology.org/2026.acl-long.419) · Zhenyu Liu, Xuanyu Zhang, Yunxin Li, Qixun Teng, Shenyuan Jiang, Haolan Chen 等

* **Mind the (DH) Gap! A Contrast in Risky Choices Between Reasoning and Conversational LLMs**
  [论文](https://aclanthology.org/2026.acl-long.479) · Luise Ge, Yongyan Zhang, Yevgeniy Vorobeychik

* **MediEval: A Unified Medical Benchmark for Patient-Contextual and Knowledge-Grounded Reasoning in LLMs**
  [论文](https://aclanthology.org/2026.acl-long.734) · Zhan Qu, Michael Farber

* **Maximizing Local Entropy Where It Matters: Prefix-Aware Localized LLM Unlearning**
  [论文](https://aclanthology.org/2026.acl-long.893) · Naixin Zhai, Pengyang Shao, Binbin Zheng, Yonghui Yang, Fei Shen, Long Bai, Xun Yang

* **GeoRA: Geometry-Aware Low-Rank Adaptation for RLVR**
  [论文](https://aclanthology.org/2026.acl-long.1110) · Jiaying Zhang, Lei Shi, Jiguo Li, Jun Xu, Jiuchong Gao, Jinghua Hao, Renqing He

* **CURE: Critique-Driven Unified Reinforcement Learning for Test-Time Self-Improvement**
  链接待补充 · Guirong Chen, Shuqi Ye, Wenkai Yang, Shiqi Shen, Guangyao Shen, Yankai Lin

* **Rethinking Entropy Interventions in RLVR: An Entropy Change Perspective**
  [论文](https://aclanthology.org/2026.acl-long.1436) · Zhezheng Hao, Hong Wang, Haoyang Liu, Jian Luo, Jiarui Yu, Hande Dong 等

* **From Local to Global: Revisiting Structured Pruning Paradigms for Large Language Models**
  [论文](https://aclanthology.org/2026.acl-long.1653) · Ziyan Wang, Enmao Diao, Qi Le, Pu Wang, Minwoo Lee, Shu-ping Yeh 等

* **CAR-bench: Evaluating the Consistency and Limit-Awareness of LLM Agents under Real-World Uncertainty**
  [论文](https://aclanthology.org/2026.acl-long.1886) · Johannes Kirmayr, Lukas Stappen, Elisabeth Andre

* **ViLL-E: Video LLM Embeddings for Retrieval**
  [论文](https://aclanthology.org/2026.acl-long.2003) · Rohit Gupta, Jayakrishnan Unnikrishnan, Fan Fei, Sheng Liu, Son Tran, Mubarak Shah

* **CxMP: A Linguistic Minimal-Pair Benchmark for Evaluating Constructional Understanding in Language Models**
  [论文](https://aclanthology.org/2026.acl-long.2132) · Miyu Oba, Saku Sugawara

* **CIG: Measuring Conversational Information Gain in Deliberative Dialogues with Semantic Memory Dynamics**
  [论文](https://aclanthology.org/2026.acl-long.2203) · Ming-Bin Chen, Jey Han Lau, Lea Frermann

* **Systematicity between Forms and Meanings across Languages Supports Efficient Communication**
  [论文](https://aclanthology.org/2026.acl-long.1340) · Doreen Osmelak, Yang Xu, Michael Hahn, Kate McCurdy
  形式和意义之间的系统性如果跨语言成立，就可以拿来解释沟通为什么能省。

* **Massively Multilingual Joint Segmentation and Glossing**
  [论文](https://aclanthology.org/2026.acl-long.1657) · Michael Ginn, Lindia Tjuatja, Enora Rice, Ali Marashian, Maria Valentini, Jasmine Xu, Graham Neubig, Alexis Palmer
  分词和注释在很多语言上一起做，而不是先切词再逐词解释。

### Best Resource Paper

* **HSCodeComp: A Realistic and Expert-level Agent Benchmark for Hierarchical Rule Application**
  [论文](https://aclanthology.org/2026.acl-long.937) · Tian Lan, Yiqian Yang, Qianghuai Jia, Li Zhu, Hui Jiang, Hang Zhu, Weihua Luo, Longyue Wang

* **ImplicitMemBench: Measuring Unconscious Behavioral Adaptation in Large Language Models**
  [论文](https://aclanthology.org/2026.acl-long.1301) · Chonghan Qin, Xiachong Feng, Weitao Ma, Xiaocheng Feng, Lingpeng Kong

* **Audio MultiChallenge: A Multi-Turn Evaluation of Spoken Dialogue Systems on Natural Human Interaction**
  [论文](https://aclanthology.org/2026.acl-long.1654) · Advait Gosai, Tyler Vuong, Utkarsh Tyagi, Steven Li, Wenjia You, Miheer Bavare 等

* **VeriTaS: The First Dynamic Benchmark for Multimodal Automated Fact-Checking**
  [论文](https://aclanthology.org/2026.acl-long.1948) · Mark Rothermel, Marcus Kornmann, Marcus Rohrbach, Anna Rohrbach

### Best Social Impact Paper

* **DIA-HARM: Dialectal Disparities in Harmful Content Detection Across 50 English Dialects**
  [论文](https://aclanthology.org/2026.acl-long.144) · Jason S Lucas, Matt Murtagh White, Ali Al-Lawati, Uchendu Uchendu, Adaku Uchendu, Dongwon Lee

* **Your Students Don't Use LLMs Like You Wish They Did**
  [论文](https://doi.org/10.48448/b40n-qe66) · Sebastian Kobler, Matthew Clemson, Angela Sun, Jonathan K. Kummerfeld

* **Afri-MCQA: Multimodal Cultural Question Answering for African Languages**
  [论文](https://doi.org/10.48448/9tw9-e625) · Atnafu Lambebo Tonja, Srija Anand, Emilio Villa-Cueva, Israel Abebe Azime, Jesujoba Oluwadara Alabi, Muhidin A Mohamed 等

### Best Theme Paper

* **CoSToM: Causal-oriented Steering for Intrinsic Theory-of-Mind Alignment in Large Language Models**
  [论文](https://aclanthology.org/2026.acl-long.421) · Mengfan Li, Xuanhua Shi, Yang Deng

* **Mapping the Circumplex of Affect: Geometric Analysis of Emotion Representations via Hyperspherical Contrastive Learning**
  [论文](https://aclanthology.org/2026.acl-long.772) · Yusuke Yamauchi, Akiko Aizawa

## 2025

### Best Paper

* **A Theory of Response Sampling in LLMs: Part Descriptive and Part Prescriptive**
  [论文](https://aclanthology.org/2025.acl-long.1454) · Sarath Sivaprasad, Pramod Kaushik, Sahar Abdelnabi, Mario Fritz
  模型采样同时在描述分布和遵守指令，这两件事不该被一个温度系数混在一起。

* **Fairness through Difference Awareness: Measuring Desired Group Discrimination in LLMs**
  [论文](https://aclanthology.org/2025.acl-long.341) · Angelina Wang, Michelle Phan, Daniel E. Ho, Sanmi Koyejo
  公平不总是抹平群体差异；有时人们要的是模型知道差异、并且用对地方。

* **Language Models Resist Alignment: Evidence From Data Compression**
  [论文](https://aclanthology.org/2025.acl-long.1141) · Jiaming Ji, Kaile Wang, Tianyi Qiu, Boyuan Chen, Jiayi Zhou, Changye Li 等
  从压缩的角度看，对齐微调很难抹掉预训练里已经写进模型的倾向。

* **Native Sparse Attention: Hardware-Aligned and Natively Trainable Sparse Attention**
  [论文](https://aclanthology.org/2025.acl-long.1126) · Jingyang Yuan, Huazuo Gao, Damai Dai, Junyu Luo, Liang Zhao, Zhengyan Zhang 等
  稀疏注意力如果不能在现代 GPU 上真的训起来，就只是纸面的复杂度。

### Outstanding Paper

* **A New Formulation of Zipf's Meaning-Frequency Law through Contextual Diversity**
  [论文](https://aclanthology.org/2025.acl-long.744) · Ryo Nagata, Kumiko Tanaka-Ishii

* **All That Glitters is Not Novel: Plagiarism in AI Generated Research**
  [论文](https://aclanthology.org/2025.acl-long.1249) · Tarun Gupta, Danish Pruthi

* **Between Circuits and Chomsky: Pre-pretraining on Formal Languages Imparts Linguistic Biases**
  [论文](https://aclanthology.org/2025.acl-long.478) · Michael Y. Hu, Jackson Petty, Chuan Shi, William Merrill, Tal Linzen

* **Beyond N-Grams: Rethinking Evaluation Metrics and Strategies for Multilingual Abstractive Summarization**
  [论文](https://aclanthology.org/2025.acl-long.932) · Itai Mondshine, Tzuf Paz-Argaman, Reut Tsarfaty

* **Bridging the Language Gaps in Large Language Models with Inference-Time Cross-Lingual Intervention**
  [论文](https://aclanthology.org/2025.acl-long.270) · Weixuan Wang, Minghao Wu, Barry Haddow, Alexandra Birch

* **Byte Latent Transformer: Patches Scale Better Than Tokens**
  [论文](https://arxiv.org/abs/2412.09871) · Artidoro Pagnoni, Ramakanth Pasunuru, Pedro Rodriguez, John Nguyen, Benjamin Muller, Margaret Li 等

* **Capability Salience Vector: Fine-grained Alignment of Loss and Capabilities for Downstream Task Scaling Law**
  [论文](https://aclanthology.org/2025.acl-long.1157) · Qiming Ge, Shuhao Xing, Songyang Gao, Yunhua Zhou, Yicheng Zou, Songyang Zhang 等

* **From Real to Synthetic: Synthesizing Millions of Diversified and Complicated User Instructions with Attributed Grounding**
  [论文](https://aclanthology.org/2025.acl-long.517) · Chiwei Zhu, Benfeng Xu, Xiaorui Wang, Zhendong Mao

* **HALOGEN: Fantastic LLM Hallucinations and Where to Find Them**
  [论文](https://aclanthology.org/2025.acl-long.71) · Abhilasha Ravichander, Shrusti Ghela, David Wadden, Yejin Choi

* **HateDay: Insights from a Global Hate Speech Dataset Representative of a Day on Twitter**
  [论文](https://aclanthology.org/2025.acl-long.115) · Manuel Tonneau, Diyi Liu, Niyati Malhotra, Scott A. Hale, Samuel Fraiberger, Victor Orozco-Olvera, Paul Röttger

* **I0T: Embedding Standardization Method Towards Zero Modality Gap**
  [论文](https://aclanthology.org/2025.acl-long.1319/) · Na Min An, Eunki Kim, James Thorne, Hyunjung Shim

* **IndicSynth: A Large-Scale Multilingual Synthetic Speech Dataset for Low-Resource Indian Languages**
  [论文](https://aclanthology.org/2025.acl-long.1070) · Divya V Sharma, Vijval Ekbote, Anubha Gupta

* **LaTIM: Measuring Latent Token-to-Token Interactions in Mamba Models**
  [论文](https://aclanthology.org/2025.acl-long.1194) · Hugo Pitorro, Marcos Vinicius Treviso

* **Llama See, Llama Do: A Mechanistic Perspective on Contextual Entrainment and Distraction in LLMs**
  [论文](https://aclanthology.org/2025.acl-long.791) · Jingcheng Niu, Xingdi Yuan, Tong Wang, Hamidreza Saghir, Amir H. Abdi

* **LLMs know their vulnerabilities: Uncover Safety Gaps through Natural Distribution Shifts**
  [论文](https://aclanthology.org/2025.acl-long.1207) · Qibing Ren, Hao Li, Dongrui Liu, Zhanxu Xie, Xiaoya Lu, Yu Qiao 等

* **Mapping 1,000+ Language Models via the Log-Likelihood Vector**
  [论文](https://aclanthology.org/2025.acl-long.1584) · Momose Oyama, Hiroaki Yamagiwa, Yusuke Takase, Hidetoshi Shimodaira

* **MiniLongBench: The Low-cost Long Context Understanding Benchmark for Large Language Models**
  [论文](https://aclanthology.org/2025.acl-long.560) · Zhongzhan Huang, Guoming Ling, Shanshan Zhong, Hefeng Wu, Liang Lin

* **PARME: Parallel Corpora for Low-Resourced Middle Eastern Languages**
  [论文](https://aclanthology.org/2025.acl-long.1451) · Sina Ahmadi, Rico Sennrich, Erfan Karami, Ako Marani, Parviz Fekrazad, Gholamreza Akbarzadeh Baghban 等

* **Past Meets Present: Creating Historical Analogy with Large Language Models**
  [论文](https://aclanthology.org/2025.acl-long.200) · Nianqi Li, Siyu Yuan, Jiangjie Chen, Jiaqing Liang, Feng Wei, Zujie Liang, Deqing Yang, Yanghua Xiao

* **Pre³: Enabling Deterministic Pushdown Automata for Faster Structured LLM Generation**
  [论文](https://aclanthology.org/2025.acl-long.551/) · Junyi Chen, Shihao Bai, Zaijun Wang, Siyu Wu, Chuheng Du, Hailong Yang 等

* **Rethinking the Role of Prompting Strategies in LLM Test-Time Scaling: A Perspective of Probability Theory**
  [论文](https://aclanthology.org/2025.acl-long.1356) · Yexiang Liu, Zekun Li, Zhi Fang, Nan Xu, Ran He, Tieniu Tan

* **Revisiting Compositional Generalization Capability of Large Language Models Considering Instruction Following Ability**
  [论文](https://aclanthology.org/2025.acl-long.1508) · Yusuke Sakai, Hidetaka Kamigaito, Taro Watanabe

* **Toward Automatic Discovery of a Canine Phonetic Alphabet**
  [论文](https://aclanthology.org/2025.acl-long.451) · Theron S. Wang, Xingyuan Li, Hridayesh Lekhak, Tuan Minh Dang, Mengyue Wu, Kenny Q. Zhu

* **Towards the Law of Capacity Gap in Distilling Language Models**
  [论文](https://aclanthology.org/2025.acl-long.1097) · Chen Zhang, Qiuchi Li, Dawei Song, Zheyu Ye, Yan Gao, Yao Hu

* **Turning Trash into Treasure: Accelerating Inference of Large Language Models with Token Recycling**
  [论文](https://aclanthology.org/2025.acl-long.338) · Xianzhen Luo, Yixuan Wang, Qingfu Zhu, Zhiming Zhang, Xuanyu Zhang, Qing Yang, Dongliang Xu

* **Typology-Guided Adaptation for African NLP**
  链接待补充 · Ndapa Nakashole

### Best Resource Paper

* **Are Rules Meant to be Broken? Understanding Multilingual Moral Reasoning as a Computational Pipeline with UniMoral**
  [论文](https://aclanthology.org/2025.acl-long.294) · Shivani Kumar, David Jurgens

* **BRIGHTER: BRIdging the Gap in Human-Annotated Textual Emotion Recognition Datasets for 28 Languages**
  [论文](https://aclanthology.org/2025.acl-long.436) · Shamsuddeen Hassan Muhammad, Nedjma Ousidhoum, Idris Abdulmumin, Jan Philip Wahle, Terry Ruas, Meriem Beloucif 等

* **Palm: A Culturally Inclusive and Linguistically Diverse Dataset for Arabic LLMs**
  [论文](https://aclanthology.org/2025.acl-long.1579) · Fakhraddin Alwajih, Abdellah EL MEKKI, Samar Mohamed Magdy, AbdelRahim A. Elmadany, OMER NACAR, El Moatez Billah Nagoudi 等

### Best Social Impact Paper

* **AfriMed-QA: A Pan-African, Multi-Specialty, Medical Question-Answering Benchmark Dataset**
  [论文](https://aclanthology.org/2025.acl-long.96) · Charles Nimo, Tobi Olatunji, Abraham Toluwase Owodunni, Tassallah Abdullahi, Emmanuel Ayodele, Mardhiyah Sanni 等

* **The AI Gap: How Socioeconomic Status Affects Language Technology Interactions**
  [论文](https://aclanthology.org/2025.acl-long.914) · Elisa Bassignana, Amanda Cercas Curry, Dirk Hovy

### Best Theme Paper

* **MaCP: Minimal yet Mighty Adaptation via Hierarchical Cosine Projection**
  [论文](https://aclanthology.org/2025.acl-long.1006) · Yixian Shen, Qi Bi, JIA-HONG HUANG, Hongyi Zhu, Andy D. Pimentel, Anuj Pathania

* **Meta-rater: A Multi-dimensional Data Selection Method for Pre-training Language Models**
  [论文](https://aclanthology.org/2025.acl-long.533) · Xinlin Zhuang, Jiahui Peng, Ren Ma, Yinfan Wang, Tianyi Bai, Xingjian Wei 等

* **SubLIME: Subset Selection via Rank Correlation Prediction for Data-Efficient LLM Evaluation**
  [论文](https://aclanthology.org/2025.acl-long.1477) · Gayathri Saranathan, Cong Xu, Mahammad Parwez Alam, Tarun Kumar, Martin Foltin, Soon Yee Wong, Suparna Bhattacharya

## 2024

### Best Paper

* **Mission: Impossible Language Models**
  [论文](https://aclanthology.org/2024.acl-long.787) · Julie Kallini, Isabel Papadimitriou, Richard Futrell, Kyle Mahowald, Christopher Potts
  用人类学不会的人造语言去探语言模型的归纳偏置：模型觉得容易的，不一定是语言学上自然的。

* **Semisupervised Neural Proto-Language Reconstruction**
  [论文](https://aclanthology.org/2024.acl-long.788) · Liang Lu, Peirong Xie, David R Mortensen

* **Why are Sensitive Functions Hard for Transformers?**
  [论文](https://aclanthology.org/2024.acl-long.800) · Michael Hahn, Mark Rofin
  有些布尔函数对 Transformer 特别难，难在架构的注意力方式，不是数据不够。

* **Natural Language Satisfiability: Exploring the Problem Distribution and Evaluating Transformer-based Language Models**
  [论文](https://aclanthology.org/2024.acl-long.815) · Tharindu Madusanka, Ian Pratt-Hartmann, Riza Batista-Navarro

* **Deciphering Oracle Bone Language with Diffusion Models**
  [论文](https://aclanthology.org/2024.acl-long.831) · Haisu Guan, Huanxin Yang, Xinyu Wang, Shengwei Han, Yongge Liu, Lianwen Jin, Xiang Bai, Yuliang Liu
  把甲骨文残片的补全写成扩散生成，古文字和现代生成模型发生了接触。

* **Causal Estimation of Memorisation Profiles**
  [论文](https://aclanthology.org/2024.acl-long.834) · Pietro Lesci, Clara Meister, Thomas Hofmann, Andreas Vlachos, Tiago Pimentel

* **Aya Model: An Instruction Finetuned Open-Access Multilingual Language Model**
  [论文](https://aclanthology.org/2024.acl-long.845) · Ahmet Üstün, Viraat Aryabumi, Zheng Xin Yong, Wei-Yin Ko, Daniel D'souza, Gbemileke Onilude 等
  把指令微调做成覆盖大量语言的开放模型，而不是只在英语上把聊天调顺。

### Outstanding Paper

* **Quantized Side Tuning: Fast and Memory-Efficient Tuning of Quantized Large Language Models**
  [论文](https://aclanthology.org/2024.acl-long.1) · Xupeng Miao, Gabriele Oliaro, Zhihao Zhang, Qing Li, Yong Jiang, Zhihao Jia

* **L-Eval: Instituting Standardized Evaluation for Long Context Language Models**
  [论文](https://aclanthology.org/2024.acl-long.776) · Chenxin An;Shansan Gong;Ming Zhong;Xingjian Zhao;Mukai Li;Jun Zhang;Lingpeng Kong;Xipeng Qiu

* **Causal-Guided Active Learning for Debiasing Large Language Models**
  [论文](https://aclanthology.org/2024.acl-long.778) · Zhouhao Sun;Li Du;Xiao Ding;Yixuan Ma;Yang Zhao;Kaitao Qiu;Ting Liu;Bing Qin

* **CausalGym: Benchmarking causal interpretability methods on linguistic tasks**
  [论文](https://aclanthology.org/2024.acl-long.785) · Aryaman Arora;Dan Jurafsky;Christopher Potts

* **Don't Hallucinate, Abstain: Identifying LLM Knowledge Gaps via Multi-LLM Collaboration**
  [论文](https://aclanthology.org/2024.acl-long.786) · Shangbin Feng;Weijia Shi;Yike Wang;Wenxuan Ding;Vidhisha Balachandran;Yulia Tsvetkov

* **Speech Translation with Speech Foundation Models and Large Language Models: What is There and What is Missing?**
  [论文](https://aclanthology.org/2024.acl-long.789) · Marco Gaido;Sara Papi;Matteo Negri;Luisa Bentivogli

* **Must NLP be Extractive?**
  [论文](https://aclanthology.org/2024.acl-long.797) · Steven Bird

* **IRCoder: Intermediate Representations Make Language Models Robust Multilingual Code Generators**
  [论文](https://aclanthology.org/2024.acl-long.802) · Indraneil Paul;Goran Glavaš;Iryna Gurevych

* **MultiLegalPile: A 689GB Multilingual Legal Corpus**
  [论文](https://aclanthology.org/2024.acl-long.805) · Joel Niklaus, Veton Matoshi, Matthias Stürmer, Ilias Chalkidis, Daniel E. Ho

* **PsySafe: A Comprehensive Framework for Psychological-based Attack, Defense, and Evaluation of Multi-agent System Safety**
  [论文](https://aclanthology.org/2024.acl-long.812) · Zaibin Zhang, Yongting Zhang, Lijun Li, Jing Shao, Hongzhi Gao, Yu Qiao 等

* **Can Large Language Models be Good Emotional Supporter? Mitigating Preference Bias on Emotional Support Conversation**
  [论文](https://aclanthology.org/2024.acl-long.813) · Dongjin Kang, Sunghwan Kim, Taeyoon Kwon, Seungjun Moon, Hyunsouk Cho, Youngjae Yu, Dongha Lee, Jinyoung Yeo

* **Political Compass or Spinning Arrow? Towards More Meaningful Evaluations for Values and Opinions in Large Language Models**
  [论文](https://aclanthology.org/2024.acl-long.816) · Paul Röttger, Valentin Hofmann, Valentina Pyatkin, Musashi Hinck, Hannah Rose Kirk, Hinrich Schuetze, Dirk Hovy

* **Same Task, More Tokens: the Impact of Input Length on the Reasoning Performance of Large Language Models**
  [论文](https://aclanthology.org/2024.acl-long.818) · Mosh Levy, Alon Jacoby, Yoav Goldberg

* **Do Llamas Work in English? On the Latent Language of Multilingual Transformers**
  [论文](https://aclanthology.org/2024.acl-long.820) · Chris Wendler, Veniamin Veselovsky, Giovanni Monea, Robert West

* **Getting Serious about Humor: Crafting Humor Datasets with Unfunny Large Language Models**
  [论文](https://aclanthology.org/2024.acl-short.76) · Zachary Horvitz, Jingru Chen, Rahul Aditya, Harshvardhan Srivastava, Robert West, Zhou Yu, Kathleen McKeown

* **Estimating the Level of Dialectness Predicts Inter-annotator Agreement in Multi-dialect Arabic Datasets**
  [论文](https://aclanthology.org/2024.acl-short.70) · Amr Keleg, Walid Magdy, Sharon Goldwater

* **G-DIG: Towards Gradient-based DIverse and hiGh-quality Instruction Data Selection for Machine Translation**
  [论文](https://aclanthology.org/2024.acl-long.821) · Xingyuan Pan, Luyang Huang, Liyan Kang, Zhicheng Liu, Yu Lu, Shanbo Cheng

* **Media Framing: A typology and Survey of Computational Approaches Across Disciplines**
  [论文](https://aclanthology.org/2024.acl-long.822) · Yulia Otmakhova, Shima Khanehzar, Lea Frermann

* **SPZ: A Semantic Perturbation-based Data Augmentation Method with Zonal-Mixing for Alzheimer's Disease Detection**
  [论文](https://aclanthology.org/2024.acl-long.823) · FangFang Li;Cheng Huang;PuZhen Su;Jie Yin

* **Greed is All You Need: An Evaluation of Tokenizer Inference Methods**
  [论文](https://aclanthology.org/2024.acl-short.73) · Omri Uzan, Craig W Schmidt, Chris Tanner, Yuval Pinter

* **Language Complexity and Speech Recognition Accuracy: Orthographic Complexity Hurts, Phonological Complexity Doesn't**
  [论文](https://aclanthology.org/2024.acl-long.827) · Chihiro Taguchi, David Chiang

* **Steering Llama 2 via Contrastive Activation Addition**
  [论文](https://aclanthology.org/2024.acl-long.828) · Nina Rimsky, Nick Gabrieli, Julian Schulz, Meg Tong, Evan J Hubinger, Alexander Matt Turner

* **EconAgent: Large Language Model-Empowered Agents for Simulating Macroeconomic Activities**
  [论文](https://aclanthology.org/2024.acl-long.829) · Nian Li, Chen Gao, Mingyu Li, Yong Li, Qingmin Liao

* **M4LE: A Multi-Ability Multi-Range Multi-Task Multi-Domain Long-Context Evaluation Benchmark for Large Language Models**
  [论文](https://aclanthology.org/2024.acl-long.832) · Wai-Chung Kwan, Xingshan Zeng, Yufei Wang, Yusen Sun, Liangyou Li, Yuxin Jiang 等

* **CHECKWHY: Causal Fact Verification via Argument Structure**
  [论文](https://aclanthology.org/2024.acl-long.835) · Jiasheng Si;Yibo Zhao;Yingjie Zhu;Haiyang Zhu;Wenpeng Lu;Deyu Zhou

* **Emulated Disalignment: Safety Alignment for Large Language Models May Backfire!**
  [论文](https://aclanthology.org/2024.acl-long.842) · Zhanhui Zhou, Jie Liu, Zhichen Dong, Jiaheng Liu, Chao Yang, Wanli Ouyang, Yu Qiao

* **IndicLLMSuite: A Blueprint for Creating Pre-training and Fine-Tuning Datasets for Indian Languages**
  [论文](https://aclanthology.org/2024.acl-long.843) · Mohammed Safi Ur Rahman Khan, Priyam Mehta, Ananth Sankar, Umashankar Kumaravelan, Sumanth Doddapaneni, Suriyaprasaad B 等

* **MultiPICo: Multilingual Perspectivist Irony Corpus**
  [论文](https://aclanthology.org/2024.acl-long.849) · Silvia Casola, Simona Frenda, Soda Marem Lo, Erhan Sezerer, Antonio Uva, Valerio Basile 等

* **MMToM-QA: Multimodal Theory of Mind Question Answering**
  [论文](https://aclanthology.org/2024.acl-long.851) · Chuanyang Jin, Yutong Wu, Jing Cao, Jiannan Xiang, Yen-Ling Kuo, Zhiting Hu 等

* **MAP's not dead yet: Uncovering true language model modes by conditioning away degeneracy**
  [论文](https://aclanthology.org/2024.acl-long.855) · Davis Yoshida, Kartik Goyal, Kevin Gimpel

* **NounAtlas: Filling the Gap in Nominal Semantic Role Labeling**
  [论文](https://aclanthology.org/2024.acl-long.857) · Roberto Navigli, Marco Lo Pinto, Pasquale Silvestri, Dennis Rotondi, Simone Ciciliano, Alessandro Scirè

* **The Earth is Flat because…: Investigating LLMs' Belief towards Misinformation via Persuasive Conversation**
  [论文](https://aclanthology.org/2024.acl-long.858) · Rongwu Xu, Brian S. Lin, Shujian Yang, Tianqi Zhang, Weiyan Shi, Tianwei Zhang 等

* **Let's Go Real Talk: Spoken Dialogue Model for Face-to-Face Conversation**
  [论文](https://aclanthology.org/2024.acl-long.860) · Se Jin Park, Chae Won Kim, Hyeongseop Rha, Minsu Kim, Joanna Hong, Jeonghun Yeo, Yong Man Ro

* **Word Embeddings Are Steers for Language Models**
  [论文](https://aclanthology.org/2024.acl-long.864) · Chi Han, Jialiang Xu, Manling Li, Yi Fung, Chenkai Sun, Nan Jiang, Tarek F. Abdelzaher, Heng Ji

* **On Efficient and Statistical Quality Estimation for Data Annotation**
  [论文](https://aclanthology.org/2024.acl-long.837/) · Jan-Christoph Klie, Juan Haladjian, Marc Kirchner, Rahul Nair
  专家不能复查全部标注时，抽查多少才能及时发现质量不够。

### Best Resource Paper

* **Latxa: An Open Language Model and Evaluation Suite for Basque**
  [论文](https://aclanthology.org/2024.acl-long.799) · Julen Etxaniz, Oscar Sainz, Naiara Perez Miguel, Itziar Aldabe, German Rigau, Eneko Agirre 等

* **Dolma: an Open Corpus of Three Trillion Tokens for Language Model Pretraining Research**
  [论文](https://aclanthology.org/2024.acl-long.840) · Luca Soldaini, Rodney Kinney, Akshita Bhagia, Dustin Schwenk, David Atkinson, Russell Authur 等
  开放预训练语料本身就是结果，否则别人无法重复你声称的训练。

* **AppWorld: A Controllable World of Apps and People for Benchmarking Interactive Coding Agents**
  [论文](https://aclanthology.org/2024.acl-long.850) · Harsh Trivedi, Tushar Khot, Mareike Hartmann, Ruskin Manku, Vinty Dong, Edward Li 等

### Best Social Impact Paper

* **How Johnny Can Persuade LLMs to Jailbreak Them: Rethinking Persuasion to Challenge AI Safety by Humanizing LLMs**
  [论文](https://aclanthology.org/2024.acl-long.773) · Yi Zeng, Hongpeng Lin, Jingwen Zhang, Diyi Yang, Ruoxi Jia, Weiyan Shi
  越狱不一定靠怪字符，普通人的说服话术就够，安全评测不该只防模板攻击。

* **DIALECTBENCH: An NLP Benchmark for Dialects, Varieties, and Closely-Related Languages**
  [论文](https://aclanthology.org/2024.acl-long.777) · Fahim Faisal, Orevaoghene Ahia, Aarohi Srivastava, Kabir Ahuja, David Chiang, Yulia Tsvetkov, Antonios Anastasopoulos

* **Having Beer after Prayer? Measuring Cultural Bias in Large Language Models**
  [论文](https://aclanthology.org/2024.acl-long.862) · Tarek Naous, Michael J Ryan, Alan Ritter, Wei Xu

### Best Theme Paper

* **OLMo: Accelerating the Science of Language Models**
  [论文](https://aclanthology.org/2024.acl-long.841) · Dirk Groeneveld, Iz Beltagy, Evan Pete Walsh, Akshita Bhagia, Rodney Kinney, Oyvind Tafjord 等
  连训练数据、代码和中间检查点一起放开，语言模型研究才有办法被别人核对。

## 2023

### Best Paper

* **Do Androids Laugh at Electric Sheep? Humor "Understanding" Benchmarks from The New Yorker Caption Contest**
  [论文](https://aclanthology.org/2023.acl-long.41) · Jack Hessel, Ana Marasovic, Jena D. Hwang, Lillian Lee, Jeff Da, Rowan Zellers, Robert Mankoff, Yejin Choi

* **What the DAAM: Interpreting Stable Diffusion Using Cross Attention**
  [论文](https://aclanthology.org/2023.acl-long.310) · Raphael Tang, Linqing Liu, Akshat Pandey, Zhiying Jiang, Gefei Yang, Karun Kumar 等
  用交叉注意力解释扩散模型生成时文本的哪些部分真正管住了图像的哪些区域。

* **From Pretraining Data to Language Models to Downstream Tasks: Tracking the Trails of Political Biases Leading to Unfair NLP Models**
  [论文](https://aclanthology.org/2023.acl-long.656) · Shangbin Feng, Chan Young Park, Yuhan Liu, Yulia Tsvetkov
  政治偏见不是在下游任务里突然出现的，可以沿着预训练数据追到模型再追到任务。

### Outstanding Paper

* **CAME: Confidence-guided Adaptive Memory Efficient Optimization**
  [论文](https://aclanthology.org/2023.acl-long.243) · Yang Luo, Xiaozhe REN, Zangwei Zheng, ZHUO JIANG, Xin Jiang, Yang You

* **Cognitive Reframing of Negative Thoughts through Human-Language Model Interaction**
  [论文](https://aclanthology.org/2023.acl-long.555) · Ashish Sharma, Kevin Rushton, Inna Lin, David Wadden, Khendra Lucas, Adam Miner, Theresa Nguyen, Tim Althoff

* **Compositional Generalization without Trees using Multiset Tagging and Latent Permutations**
  [论文](https://aclanthology.org/2023.acl-long.810) · Matthias Lindemann, Alexander Koller, Ivan Titov

* **Considerations for meaningful sign language machine translation based on glosses**
  [论文](https://aclanthology.org/2023.acl-short.60) · Mathias Müller, Zifan Jiang, Amit Moryossef, Annette Rios, Sarah Ebling

* **Dense-ATOMIC: Towards Densely-connected ATOMIC with High Knowledge Coverage and Massive Multi-hop Paths**
  [论文](https://aclanthology.org/2023.acl-long.742) · Xiangqing Shen, Siwei Wu, Rui Xia

* **Dissecting Transformer Length Extrapolation via the Lens of Receptive Field Analysis**
  [论文](https://aclanthology.org/2023.acl-long.756) · Ta-Chung Chi, Ting-Han Fan, alexander rudnicky, Peter Ramadge

* **Distilling Script Knowledge from Large Language Models for Constrained Language Planning**
  [论文](https://aclanthology.org/2023.acl-long.236) · Siyu Yuan, Jiangjie Chen, Ziquan Fu, Xuyang Ge, Soham Shah, Charles Jankowski, Yanghua Xiao, Deqing Yang

* **Do PLMs Know and Understand Ontological Knowledge?**
  [论文](https://aclanthology.org/2023.acl-long.173) · Weiqi Wu, Chengyue Jiang, Yong Jiang, Pengjun Xie, Kewei Tu

* **Don't Generate, Discriminate: A Proposal for Grounding Language Models to Real-World Environments**
  [论文](https://aclanthology.org/2023.acl-long.270) · Yu Gu, Xiang Deng, Yu Su

* **Extrinsic Evaluation of Machine Translation Metrics**
  [论文](https://aclanthology.org/2023.acl-long.730) · Nikita Moghe, Tom Sherborne, Mark Steedman, Alexandra Birch

* **Faithful Low-Resource Data-to-Text Generation through Cycle Training**
  [论文](https://aclanthology.org/2023.acl-long.160) · Zhuoer Wang, Marcus Collins, Nikhita Vedula, Simone Filice, Shervin Malmasi, Oleg Rokhlenko

* **Generalizing Backpropagation for Gradient-Based Interpretability**
  [论文](https://aclanthology.org/2023.acl-long.669) · Kevin Du, Lucas Torroba Hennigen, Niklas Stoehr, Alex Warstadt, Ryan Cotterell

* **Hexatagging: Projective Dependency Parsing as Tagging**
  [论文](https://aclanthology.org/2023.acl-short.124) · Afra Amini, Tianyu Liu, Ryan Cotterell

* **Hybrid Transducer and Attention based Encoder-Decoder Modeling for Speech-to-Text Tasks**
  [论文](https://aclanthology.org/2023.acl-long.695) · Yun Tang, Anna Sun, Hirofumi Inaguma, Xinyue Chen, Ning Dong, Xutai Ma, Paden Tomasello, Juan Pino

* **Improving Pretraining Techniques for Code-Switched NLP**
  [论文](https://aclanthology.org/2023.acl-long.66) · Richeek Das, Sahasra Ranjan, Shreya Pathak, Preethi Jyothi

* **Knowledge Transfer in Incremental Learning for Multilingual Neural Machine Translation**
  [论文](https://aclanthology.org/2023.acl-long.852) · Kaiyu Huang, Peng Li, Jin Ma, Ting Yao, Yang Liu

* **Language model acceptability judgements are not always robust to context**
  [论文](https://aclanthology.org/2023.acl-long.333) · Koustuv Sinha, Jon Gauthier, Aaron Mueller, Kanishka Misra, Keren Fuentes, Roger Levy, Adina Williams

* **Linear Classifier: An Often-Forgotten Baseline for Text Classification**
  [论文](https://aclanthology.org/2023.acl-short.160) · Yu-Chen Lin, Si-An Chen, Jie-Jyun Liu, Chih-Jen Lin

* **Minding Language Models' (Lack of) Theory of Mind: A Plug-and-Play Multi-Character Belief Tracker**
  [论文](https://aclanthology.org/2023.acl-long.780) · Melanie Sclar, Sachin Kumar, Peter West, Alane Suhr, Yejin Choi, Yulia Tsvetkov

* **MultiInstruct: Improving Multi-Modal Zero-Shot Learning via Instruction Tuning**
  [论文](https://aclanthology.org/2023.acl-long.641) · Zhiyang Xu, Ying Shen, Lifu Huang

* **Multilingual LLMs are Better Cross-lingual In-context Learners with Alignment**
  [论文](https://aclanthology.org/2023.acl-long.346) · Eshaan Tanwar, Subhabrata Dutta, Manish Borthakur, Tanmoy Chakraborty

* **Neural Machine Translation Methods for Translating Text to Sign Language Glosses**
  [论文](https://aclanthology.org/2023.acl-long.700) · Dele Zhu, Vera Czehmann, Eleftherios Avramidis

* **NLPositionality: Characterizing Design Biases of Datasets and Models**
  [论文](https://aclanthology.org/2023.acl-long.505) · Sebastin Santy, Jenny Liang, Ronan Le Bras, Katharina Reinecke, Maarten Sap

* **PeaCoK: Persona Commonsense Knowledge for Consistent and Engaging Narratives**
  [论文](https://aclanthology.org/2023.acl-long.362) · Silin Gao, Beatriz Borges, Soyoung Oh, Deniz Bayazit, Saya Kanno, Hiromi Wakaki, Yuki Mitsufuji, Antoine Bosselut

* **QUEST: A Retrieval Dataset of Entity-Seeking Queries with Implicit Set Operations**
  [论文](https://aclanthology.org/2023.acl-long.784) · Chaitanya Malaviya, Peter Shaw, Ming-Wei Chang, Kenton Lee, Kristina Toutanova

* **Question-Answering in a Low-resourced Language: Benchmark Dataset and Models for Tigrinya**
  [论文](https://aclanthology.org/2023.acl-long.661) · Fitsum Gaim, Wonsuk Yang, Hancheol Park, Jong Park

* **Scaling in Cognitive Modelling: a Multilingual Approach to Human Reading Times**
  [论文](https://aclanthology.org/2023.acl-short.14) · Andrea Gregor de Varda, Marco Marelli

* **SCOTT: Self-Consistent Chain-of-Thought Distillation**
  [论文](https://aclanthology.org/2023.acl-long.304) · Peifeng Wang, Zhengyang Wang, Zheng Li, Yifan Gao, Bing Yin, Xiang Ren

* **The Mechanical Bard: An Interpretable Machine Learning Approach to Shakespearean Sonnet Generation**
  [论文](https://aclanthology.org/2023.acl-short.140) · Edwin Agnew, Michelle Qiu, Lily Zhu, Sam Wiseman, Cynthia Rudin

* **The Tail Wagging the Dog: Dataset Construction Biases of Social Bias Benchmarks**
  [论文](https://aclanthology.org/2023.acl-short.118) · Nikil Selvam, Sunipa Dev, Daniel Khashabi, Tushar Khot, Kai-Wei Chang

* **Towards Zero-Shot Multilingual Transfer for Code-Switched Responses**
  [论文](https://aclanthology.org/2023.acl-long.417) · Ting-Wei Wu, Changsheng Zhao, Ernie Chang, Yangyang Shi, Pierce Chuang, Vikas Chandra, Biing Juang

* **Transfer and Active Learning for Dissonance Detection: Addressing the Rare-Class Challenge**
  [论文](https://aclanthology.org/2023.acl-long.665) · Vasudha Varadarajan, Swanie Juhng, Syeda Mahwish, Xiaoran Liu, Jonah Luby, Christian Luhmann, H. Andrew Schwartz

* **VisText: A Benchmark for Semantically Rich Chart Captioning**
  [论文](https://aclanthology.org/2023.acl-long.401) · Benny Tang, Angie Boggust, Arvind Satyanarayan

* **What's the Meaning of Superhuman Performance in Today's NLU?**
  [论文](https://aclanthology.org/2023.acl-long.697) · Simone Tedeschi, Johan Bos, Thierry Declerck, Jan Hajič, Daniel Hershcovich, Eduard Hovy 等

* **WikiBio: a Semantic Resource for the Intersectional Analysis of Biographical Events**
  [论文](https://doi.org/10.5281/zenodo.7656861) · Marco Antonio Stranisci, Rossana Damiano, Enrico Mensa, Viviana Patti, Daniele Radicioni, Tommaso Caselli

* **World-to-Words: Grounded Open Vocabulary Acquisition through Fast Mapping in Vision-Language Models**
  [论文](https://aclanthology.org/2023.acl-long.31) · Ziqiao Ma, Jiayi Pan, Joyce Chai

* **Backpack Language Models**
  [论文](https://aclanthology.org/2023.acl-long.506) · John Hewitt, John Thickstun, Christopher Manning, Percy Liang
  把词的意义拆成可以相加的非上下文分量，再看模型预测时用了哪一个分量。

* **Causes and Cures for Interference in Multilingual Translation**
  [论文](https://aclanthology.org/2023.acl-long.883/) · Uri Shaham, Maha Elbayad, Vedanuj Goswami, Omer Levy, Shruti Bhosale
  多语言翻译里语言之间会互相干扰，这篇把干扰的来源和缓解放在一起看。

### Honorable Mention

* **ByGPT5: End-to-End Style-conditioned Poetry Generation with Token-free Language Models**
  [论文](https://aclanthology.org/2023.acl-long.406) · Jonas Belouadi, Steffen Eger

* **DiffusionDB: A Large-scale Prompt Gallery Dataset for Text-to-Image Generative Models**
  [论文](https://aclanthology.org/2023.acl-long.51) · Zijie J. Wang, Evan Montoya, David Munechika, Haoyang Yang, Benjamin Hoover, Duen Horng Chau

* **DrBERT: A Robust Pre-trained Model in French for Biomedical and Clinical domains**
  [论文](https://aclanthology.org/2023.acl-long.896) · Yanis Labrak, Adrien Bazoge, Richard Dufour, Mickael Rouvier, Emmanuel Morin, Béatrice Daille, Pierre-Antoine Gourraud

* **Entity Tracking in Language Models**
  [论文](https://aclanthology.org/2023.acl-long.213) · Najoung Kim, Sebastian Schuster

* **Forgotten Knowledge: Examining the Citational Amnesia in NLP**
  [论文](https://aclanthology.org/2023.acl-long.341) · Janvijay Singh, Mukund Rungta, Diyi Yang, Saif Mohammad

* **From Characters to Words: Hierarchical Pre-trained Language Model for Open-vocabulary Language Understanding**
  [论文](https://aclanthology.org/2023.acl-long.200) · Li Sun, Florian Luisier, Kayhan Batmanghelich, Dinei Florencio, Cha Zhang

* **GIFT: Graph-Induced Fine-Tuning for Multi-Party Conversation Understanding**
  [论文](https://aclanthology.org/2023.acl-long.651) · Jia-Chen Gu, Zhenhua Ling, Quan Liu, Cong Liu, Guoping Hu

* **Latent Positional Information is in the Self-Attention Variance of Transformer Language Models Without Positional Embeddings**
  [论文](https://aclanthology.org/2023.acl-short.102) · Ta-Chung Chi, Ting-Han Fan, Li-Wei Chen, alexander rudnicky, Peter Ramadge

* **Revisiting non-English Text Simplification: A Unified Multilingual Benchmark**
  [论文](https://aclanthology.org/2023.acl-long.269) · Michael Ryan, Tarek Naous, Wei Xu

* **Synthetic Text Generation with Differential Privacy: A Simple and Practical Recipe**
  [论文](https://aclanthology.org/2023.acl-long.74) · Xiang Yue, Huseyin Inan, Xuechen Li, Girish Kumar, Julia McAnallen, Hoda Shajari 等

* **Theory-Grounded Computational Text Analysis**
  [论文](https://aclanthology.org/2023.acl-short.136) · Arya D. McCarthy, Giovanna Maria Dora Dore

* **Towards Understanding Chain-of-Thought Prompting: An Empirical Study of What Matters**
  [论文](https://aclanthology.org/2023.acl-long.153) · Boshi Wang, Sewon Min, Xiang Deng, Jiaming Shen, You Wu, Luke Zettlemoyer, Huan Sun

* **UniCoRN: Unified Cognitive Signal ReconstructioN bridging cognitive signals and human language**
  [论文](https://aclanthology.org/2023.acl-long.741) · Nuwa Xi, Sendong Zhao, Haochun Wang, Chi Liu, Bing Qin, Ting Liu

* **Human Inspired Progressive Alignment and Comparative Learning for Grounded Word Acquisition**
  [论文](https://aclanthology.org/2023.acl-long.863/) · Yuwei Bao, Barrett Lattimer, Joyce Chai
  用比较属性异同的过程，让模型在很少的样本里抽出同一个词所指的共同东西。

### Social Impact Award

* **Marked Personas: Using Natural Language Prompts to Measure Stereotypes in Language Models**
  [论文](https://aclanthology.org/2023.acl-long.84) · Myra Cheng, Esin Durmus, Dan Jurafsky

### Resource Award

* **When Does Translation Require Context? A Data-driven, Multilingual Exploration**
  [论文](https://aclanthology.org/2023.acl-long.36) · Patrick Fernandes, Kayo Yin, Emmy Liu, André Martins, Graham Neubig

### Reproduction Award

* **Do CoNLL-2003 Named Entity Taggers Still Work Well in 2023?**
  [论文](https://aclanthology.org/2023.acl-long.459) · Shuheng Liu, Alan Ritter

### Theme Paper Award

* **Weaker Than You Think: A Critical Look at Weakly Supervised Learning**
  [论文](https://aclanthology.org/2023.acl-long.796) · Dawei Zhu, Xiaoyu Shen, Marius Mosbach, Andreas Stephan, Dietrich Klakow

## 2022

### Best Paper

* **Learned Incremental Representations for Parsing**
  [论文](https://aclanthology.org/2022.acl-long.220/) · Nikita Kitaev, Thomas Lu, Dan Klein
  每个词只在看到前缀时打一个离散标签，标签序列就能确定句法树，从而让分析真正是增量的。

### Outstanding Paper

* **Evaluating Factuality in Text Simplification**
  [论文](https://aclanthology.org/2022.acl-long.506/) · Ashwin Devaraj, William Berkeley Sheffield, Byron C. Wallace, Junyi Jessy Li
  简化文本很容易把事实改掉，评测必须单独看事实还在不在。

* **Online Semantic Parsing for Latency Reduction in Task-Oriented Dialogue**
  [论文](https://aclanthology.org/2022.acl-long.110) · Jiawei Zhou, Jason Eisner, Michael Newman, Emmanouil Antonios Platanios, Sam Thomson
  任务型对话不必等整句说完再解析，在线解析是为了把延迟降下来。

* **Learning to Generalize to More: Continuous Semantic Augmentation for Neural Machine Translation**
  [论文](https://aclanthology.org/2022.acl-long.546/) · Xiangpeng Wei, Heng Yu, Yue Hu, Rongxiang Weng, Weihua Luo, Rong Jin
  翻译的泛化可以靠连续的语义增广，而不是只换一批平行句。

* **Fantastically Ordered Prompts and Where to Find Them: Overcoming Few-Shot Prompt Order Sensitivity**
  [论文](https://aclanthology.org/2022.acl-long.556) · Yao Lu, Max Bartolo, Alastair Moore, Sebastian Riedel, Pontus Stenetorp
  少样本提示的顺序本身就会翻盘，找顺序是方法的一部分。

* **Inducing Positive Perspectives with Text Reframing**
  [论文](https://aclanthology.org/2022.acl-long.257) · Caleb Ziems, Minzhi Li, Anthony Zhang, Diyi Yang
  换一种说法可以改变视角，这是生成问题，也是社会语言学问题。

* **Ditch the Gold Standard: Re-evaluating Conversational Question Answering**
  [论文](https://aclanthology.org/2022.acl-long.555) · Huihan Li, Tianyu Gao, Manan Goenka, Danqi Chen
  对话问答的金标准评测和真实对话并不一样，需要把评测本身拿出来重做。

* **Active Evaluation: Efficient NLG Evaluation with Few Pairwise Comparisons**
  [论文](https://aclanthology.org/2022.acl-long.600) · Akash Kumar Mohankumar, Mitesh M. Khapra
  生成评测不必两两比完，主动选择比较可以少问很多次。

* **Compression of Generative Pre-trained Language Models via Quantization**
  [论文](https://aclanthology.org/2022.acl-long.331/) · Chaofan Tao, Lu Hou, Wei Zhang, Lifeng Shang, Xin Jiang, Qun Liu, Ping Luo, Ngai Wong
  生成式预训练模型的压缩要面对生成，而不只是分类精度。

### Best Special Theme Paper

* **Requirements and Motivations of Low-Resource Speech Synthesis for Language Revitalization**
  [论文](https://aclanthology.org/2022.acl-long.507/) · Aidan Pine, Dan Wells, Nathan Brinklow, Patrick William Littell, Korin Richmond
  把低资源语音合成放回语言复兴的真实需求，而不是默认技术指标就是社区要的东西。

### Best Linguistic Insight Paper

* **KinyaBERT: a Morphology-aware Kinyarwanda Language Model**
  [论文](https://aclanthology.org/2022.acl-long.367/) · Antoine Nzeyimana, Andre Niyongabo Rubungo
  形态丰富的语言不该被当成缺数据的英语；模型要先承认词的内部结构。

### Best Resource Paper

* **DiBiMT: A Novel Benchmark for Measuring Word Sense Disambiguation Biases in Machine Translation**
  [论文](https://aclanthology.org/2022.acl-long.298) · Niccolò Campolungo, Federico Martelli, Francesco Saina, Roberto Navigli
  机器翻译里的词义偏见需要专门的基准，不能只看 BLEU。

# EMNLP

## 2026

### Best Paper

* **DiscoTrace: Representing and Comparing Answering Strategies of Humans and LLMs in Information-Seeking Question Answering**
  [论文](https://arxiv.org/abs/2604.15140) · Neha Srikanth, Jordan Boyd-Graber, Rachel Rudinger
  人回答信息寻求问题的策略和模型不一样；先把策略表示出来，才能比较，而不是只比最后一句对不对。

* **Don't Read Everything: A Curvature-Conditioned Query for Linear Attention**
  [论文](https://arxiv.org/abs/2606.01294) · Dong Le, Thong Thanh Nguyen, Cong-Duy T Nguyen, Anh Tuan Luu
  线性注意力不该对所有位置一视同仁，查询可以按曲率决定哪里值得读。

### Outstanding Paper

* **Accelerating Constrained Decoding with Token Space Compression**
  [论文](https://arxiv.org/abs/2605.29986) · Michael Sullivan, Alexander Koller

* **Rethinking the Evaluation of Efficiency Methods for Multi-Agent Systems**
  [论文](https://arxiv.org/abs/2609.05933) · Jiamu Zhang, Lingxi Zhang, Pengjun Lu, Qiyue Zhang, Yu-Neng Chuang, Zhengchen Li 等

* **SkillHarm: Lifecycle-Aware Skill-Based Attacks via Automated Construction**
  [论文](https://arxiv.org/abs/2606.02540) · Yuting Ning, Zhehao Zhang, Yash Kumar Lal, Boyu Gou, Junyi Li, Weitong Ruan 等

* **Counterfactual Constraint-Conditioned On-Policy Distillation for Multi-Constraint Instruction Following**
  [论文](https://doi.org/10.18653/2026.emnlp-main.1037) · Yanzhao Zheng, Yuanqiang Yu, Tianze Xu, Chao Ma, Zhentao Zhang, Jihuai Zhu 等

* **OptiMer: Optimal Distribution Vector Merging Is Better than Data Mixing for Continual Pre-Training**
  [论文](https://doi.org/10.18653/2026.emnlp-main.1090) · Haiyue Song, Huy Hien Vu, Masao Utiyama

* **Can MLLMs Perceive and Describe Medical Image Quality Beyond Scores?**
  [论文](https://arxiv.org/abs/2510.01691) · Jiyao Liu, Jinjie Wei, Wanying Qu, Chenglong Ma, Junzhi Ning, Yunheng Li 等

* **Omnilingual MT: Machine Translation for 1,600 Languages**
  链接待补充 · Belen Alastruey, Niyati Bafna, Andrea Caciolai, Kevin Heffernan, Artyom Kozhevnikov, Christophe Ropers 等

* **Do Benchmarks Measure the Same Thing? Evaluation-Free Benchmark Redundancy Analysis with SAE**
  [论文](https://doi.org/10.18653/2026.emnlp-main.1284) · Yaoning Wang, Jiahao Ying, Yubo Ma, Yu Wan, Dayiheng Liu, Yixin Cao, Yu-Gang Jiang

* **UReason: Benchmarking Reasoning-to-Generation Alignment in Unified Multimodal Models**
  [论文](https://arxiv.org/abs/2602.08336) · Cheng Yang, Chufan Shi, Bo Shui, Yaokang Wu, Muzi Tao, Huijuan Wang 等

* **In-Place Feedback: Reliable Refinement for Multi-Turn Expert-LLM Collaboration**
  [论文](https://arxiv.org/abs/2510.00777) · Youngbin Choi, Minjong Lee, Saemi Moon, Seunghyuk Cho, Chaehyeon Chung, MoonJeong Park, Dongwoo Kim

* **D3-Gym: Constructing Real-World Verifiable Environments for Data-Driven Discovery**
  [论文](https://arxiv.org/abs/2604.27977) · Hanane Nour Moussa, Yifei Li, Zhuoyang Li, Yankai Yang, Cheng Tang, Tianshu Zhang 等

* **The Cost of Sounding Different: Accent Bias in Audio Language Models**
  [论文](https://doi.org/10.18653/2026.emnlp-main.1612) · Aruna Srivastava, Orevaoghene Ahia, Li Lucy, Ashley Christendat, Sameep Chattopadhyay, Farhan Samir 等

* **From Token Probabilities to Semantic Constraints: Towards Declarative Probabilistic Evaluation of Language Models**
  链接待补充 · Kyle Richardson, Cullen Anderson, Pranav Balakrishnan, Takuto Ban, Daksha Ladia, Ankita Gupta, Marisa Hudspeth

* **Conformal Certification of Reasoning Trace Prefixes**
  [论文](https://arxiv.org/abs/2605.30085) · Matt Y. Cheung, Ashok Veeraraghavan, Hanjie Chen, Guha Balakrishnan

* **When Must Faithful Chain-of-Thought Fail? An Information-Theoretic Bound and Its Empirical Limits**
  [论文](https://doi.org/10.18653/2026.emnlp-main.1823) · Jikun Wu, Dongxin Guo, SM Yiu

* **Diffusion Large Language Models for Visual Speech Recognition**
  [论文](https://arxiv.org/abs/2605.28456) · Jeong Hun Yeo, Chae Won Kim, Hyeongseop Rha, Yong Man Ro

* **Race in the Record: Measuring Racial Signal and Model Inference in Police Arrest Narratives**
  [论文](https://doi.org/10.18653/2026.emnlp-main.1850) · Arka Dutta, Ted Forsyth, O. Nicholas Robertson, Ashiqur R. KhudaBukhsh

* **Aligned but Not Partner-Specific: How Multimodal LLM Agents Succeed in Reference Games Without Forming Conceptual Pacts**
  [论文](https://arxiv.org/abs/2606.08081) · Po-Ya Angela Wang, Chinmaya Mishra, Asli Ozyurek, Paula Rubio-Fernandez, Esam Ghaleb

* **Format as Nuisance: Intervention-Inspired Cross-Format Distillation for Knowledge Conflicts**
  [论文](https://doi.org/10.18653/2026.emnlp-main.2028) · Yue Yu, Wang Luo, Shenghao Ye, Zepeng Bao, Jiacheng Liu, Yongqi Li, Wenxin Tang, Tieyun Qian

* **Double Trouble: Bilingual Pretraining Leaves Language-Conditioned Effects in Shared-Language Representations**
  [论文](https://arxiv.org/abs/2608.26576) · Anjishnu Mukherjee, Ziwei Zhu, Antonios Anastasopoulos

* **Language Identification for Non-Standard Varieties: Language Varieties as Geolects on a Geodesic Grid**
  [论文](https://doi.org/10.18653/2026.emnlp-main.2175) · Sina Ahmadi, Rico Sennrich

* **Accountable AI with Grounded, Faithful, Consistent, Actionable Rationales: A Case Study in Clinical Trial Matching with VERDICT**
  [论文](https://arxiv.org/abs/2609.03366) · Zikai Zhou, Yufei Jin, Yilin Xu, Yu-Chiang Wang, Chieh-Ju Chao, Monica Lam

### Best Special Theme Paper

* **Beyond "To whom it may concern": Tailoring Machine Translation to Audience and Intent**
  [论文](https://arxiv.org/abs/2606.03259) · Raphaël Merx, Ekaterina Vylomova, Trevor Cohn

### Best Resource Paper

* **XYBench: Can LLMs Respond Pragmatically to Queries with Misconceptions?**
  [论文](https://arxiv.org/abs/2609.06842) · Akhila Yerukola, Jena D. Hwang, Mingqian Zheng, Jenna Godsey, Hyunwoo Kim, Valentina Pyatkin, Jennifer Hu, Maarten Sap

### Social Impact Award

* **Clinically Grounded Privacy Evaluation of Medical LMs**
  [论文](https://arxiv.org/abs/2606.09590) · Sasha Ronaghi, Sana Tonekaboni, Lena Stempfle, Vivian Utti, Jordan Li Cahoon, Nathaniel Hendrix 等

## 2025

### Best Paper

* **Infini-gram mini: Exact n-gram Search at the Internet Scale with FM-Index**
  [论文](https://aclanthology.org/2025.emnlp-main.1268) · Hao Xu, Jiacheng Liu, Yejin Choi, Noah A. Smith, Hannaneh Hajishirzi
  把精确 n-gram 检索做到互联网规模，用来核对模型到底见过没有，而不是再近似一次。

### Outstanding Paper

* **LingGym: How Far Are LLMs from Thinking Like Field Linguists?**
  [论文](https://aclanthology.org/2025.emnlp-main.69) · Changbing Yang, Franklin Ma, Freda Shi, Jian Zhu

* **Mind the Value-Action Gap: Do LLMs Act in Alignment with Their Values?**
  [论文](https://aclanthology.org/2025.emnlp-main.154) · Hua Shen, Nicholas Clark, Tanu Mitra

* **DiscoSG: Towards Discourse-Level Text Scene Graph Parsing through Iterative Graph Refinement**
  [论文](https://aclanthology.org/2025.emnlp-main.398) · Shaoqing Lin, Chong Teng, Fei Li, Donghong Ji, Lizhen Qu, Zhuang Li

* **Generative or Discriminative? Revisiting Text Classification in the Era of Transformers**
  [论文](https://aclanthology.org/2025.emnlp-main.486) · Siva Rajesh Kasa, Karan Gupta, Sumegh Roychowdhury, Ashutosh Kumar

* **Measuring Chain of Thought Faithfulness by Unlearning Reasoning Steps**
  [论文](https://aclanthology.org/2025.emnlp-main.504) · Martin Tutek, Fateme Hashemi Chaleshtori, Ana Marasovic, Yonatan Belinkov
  把思维链里的步骤忘掉再看答案变不变，用来检验链是不是真的在起作用。

* **MiCRo: Mixture Modeling and Context-aware Routing for Personalized Preference Learning**
  [论文](https://aclanthology.org/2025.emnlp-main.882) · Jingyan Shen, Jiarui Yao, Rui Yang, Yifan Sun, Feng Luo, Rui Pan, Tong Zhang, Han Zhao

* **Causal Interventions Reveal Shared Structure Across English Filler-Gap Constructions**
  [论文](https://aclanthology.org/2025.emnlp-main.1271) · Sasha Boguraev, Christopher Potts, Kyle Mahowald

### Best Special Theme Paper

* **InterIDEAS: Philosophical Intertextuality via LLMs**
  [论文](https://aclanthology.org/2025.emnlp-main.1180) · Yue Yang, Yinzhi Xu, Chenghao Huang, JohnMichael Jurgensen, Han Hu, Hao Wang

### Best Resource Paper

* **Autoformalization in the Wild: Assessing LLMs on Real-World Mathematical Definitions**
  [论文](https://aclanthology.org/2025.emnlp-main.90) · Lan Zhang, Marco Valentino, Andre Freitas

### People's Choice Award

* **Randomly Removing 50% of Dimensions in Text Embeddings has Minimal Impact on Retrieval and Classification Tasks**
  [论文](https://aclanthology.org/2025.emnlp-main.1410) · Sotaro Takeshita, Yurina Takeshita, Daniel Ruffinelli, Simone Paolo Ponzetto

### Social Impact Award

* **AccessEval: Benchmarking Disability Bias in Large Language Models**
  [论文](https://aclanthology.org/2025.emnlp-main.1653) · Srikant Panda, Amit Agarwal, Hitesh Laxmichand Patel

## 2024

### Best Paper

* **An image speaks a thousand words, but can everyone listen? On image transcreation for cultural relevance**
  [论文](https://aclanthology.org/2024.emnlp-main.573) · Simran Khanuja, Sathyanarayanan Ramamoorthy, Yueqi Song, Graham Neubig

* **Towards Robust Speech Representation Learning for Thousands of Languages**
  [论文](https://aclanthology.org/2024.emnlp-main.570) · William Chen, Wangyou Zhang, Yifan Peng, Xinjian Li, Jinchuan Tian, Jiatong Shi 等

* **Backward Lens: Projecting Language Model Gradients into the Vocabulary Space**
  [论文](https://aclanthology.org/2024.emnlp-main.142) · Shahar Katz, Yonatan Belinkov, Mor Geva, Lior Wolf

* **Pretraining Data Detection for Large Language Models: A Divergence-based Calibration Method**
  [论文](https://aclanthology.org/2024.emnlp-main.300) · Weichao Zhang, Ruqing Zhang, Jiafeng Guo, Maarten de Rijke, Yixing Fan, Xueqi Cheng

* **CoGen: Learning from Feedback with Coupled Comprehension and Generation**
  [论文](https://aclanthology.org/2024.emnlp-main.721) · Mustafa Omer Gul, Yoav Artzi

### Outstanding Paper

* **Fishing for Magikarp: Automatically Detecting Under-trained Tokens in Large Language Models**
  [论文](https://aclanthology.org/2024.emnlp-main.649) · Sander Land, Max Bartolo

* **Learning to Retrieve Iteratively for In-Context Learning**
  [论文](https://aclanthology.org/2024.emnlp-main.406) · Yunmo Chen, Tongfei Chen, Harsh Jhamtani, Patrick Xia, Richard Shin, Jason Eisner, Benjamin Van Durme

* **Measuring Psychological Depth in Language Models**
  [论文](https://aclanthology.org/2024.emnlp-main.953/) · Fabrice Y Harel-Canada, Hanyu Zhou, Sreya Muppalla, Zeynep Senahan Yildiz, Miryung Kim, Amit Sahai, Nanyun Peng

* **Do LLMs Plan Like Human Writers? Comparing Journalist Coverage of Press Releases with LLMs**
  [论文](https://aclanthology.org/2024.emnlp-main.1216) · Alexander Spangher, Nanyun Peng, Sebastian Gehrmann, Mark Dredze

* **Words Worth a Thousand Pictures: Measuring and Understanding Perceptual Variability in Text-to-Image Generation**
  [论文](https://aclanthology.org/2024.emnlp-main.311) · Raphael Tang, Crystina Zhang, Lixinyu Xu, Yao Lu, Wenyan Li, Pontus Stenetorp, Jimmy Lin, Ferhan Ture

* **Finding Blind Spots in Evaluator LLMs with Interpretable Checklists**
  [论文](https://aclanthology.org/2024.emnlp-main.911) · Sumanth Doddapaneni, Mohammed Safi Ur Rahman Khan, Sshubam Verma, Mitesh M Khapra

* **GoldCoin: Grounding Large Language Models in Privacy Laws via Contextual Integrity Theory**
  [论文](https://aclanthology.org/2024.emnlp-main.195) · Wei Fan, Haoran Li, Zheye Deng, Weiqi Wang, Yangqiu Song

* **Verification and Refinement of Natural Language Explanations through LLM-Symbolic Theorem Proving**
  [论文](https://aclanthology.org/2024.emnlp-main.172) · Xin Quan, Marco Valentino, Louise A. Dennis, Andre Freitas

* **The Zeno's Paradox of ‘Low-Resource' Languages**
  [论文](https://aclanthology.org/2024.emnlp-main.983) · Hellina Hailu Nigatu, Atnafu Lambebo Tonja, Benjamin Rosman, Thamar Solorio, Monojit Choudhury

* **When Is Multilinguality a Curse? Language Modeling for 250 High- and Low-Resource Languages**
  [论文](https://aclanthology.org/2024.emnlp-main.236) · Tyler A. Chang, Catherine Arnett, Zhuowen Tu, Ben Bergen

* **Language Models Learn Rare Phenomena from Less Rare Phenomena: The Case of the Missing AANNs**
  [论文](https://aclanthology.org/2024.emnlp-main.53) · Kanishka Misra, Kyle Mahowald

* **Fool Me Once? Contrasting Textual and Visual Explanations in a Clinical Decision-Support Setting**
  [论文](https://aclanthology.org/2024.emnlp-main.1051) · Maxime Guillaume Kayser, Bayar Menzat, Cornelius Emde, Bogdan Alexandru Bercean, Alex Novak, Abdalá Trinidad Espinosa Morgado 等

* **Threshold-driven Pruning with Segmented Maximum Term Weights for Approximate Cluster-based Sparse Retrieval**
  [论文](https://aclanthology.org/2024.emnlp-main.1101) · Yifan Qiao, Parker Carlson, Shanxiu He, Yingrui Yang, Tao Yang

* **Are Large Language Models Capable of Generating Human-Level Narratives?**
  [论文](https://aclanthology.org/2024.emnlp-main.978) · Yufei Tian, Tenghao Huang, Miri Liu, Derek Jiang, Alexander Spangher, Muhao Chen, Jonathan May, Nanyun Peng

* **Formality is Favored: Unraveling the Learning Preferences of Large Language Models on Data with Conflicting Knowledge**
  [论文](https://aclanthology.org/2024.emnlp-main.304) · Jiahuan Li, Yiqing Cao, Shujian Huang, Jiajun Chen

* **OATH-Frames: Characterizing Online Attitudes Towards Homelessness with LLM Assistants**
  [论文](https://aclanthology.org/2024.emnlp-main.724) · Jaspreet Ranjit, Brihi Joshi, Rebecca Dorn, Laura Petry, Olga Koumoundouros, Jayne Bottarini 等

* **SUPER: Evaluating Agents on Setting Up and Executing Tasks from Research Repositories**
  [论文](https://aclanthology.org/2024.emnlp-main.702) · Ben Bogin, Kejuan Yang, Shashank Gupta, Kyle Richardson, Erin Bransom, Peter Clark, Ashish Sabharwal, Tushar Khot

* **Towards Cross-Cultural Machine Translation with Retrieval-Augmented Generation from Multilingual Knowledge Graphs**
  [论文](https://aclanthology.org/2024.emnlp-main.914) · Simone Conia, Daniel Lee, Min Li, Umar Farooq Minhas, Saloni Potdar, Yunyao Li

* **Which questions should I answer? Salience Prediction of Inquisitive Questions**
  [论文](https://aclanthology.org/2024.emnlp-main.1114) · Yating Wu, Ritika Rajesh Mangla, Alex Dimakis, Greg Durrett, Junyi Jessy Li

* **Learning Planning-based Reasoning by Trajectories Collection and Process Reward Synthesizing**
  [论文](https://aclanthology.org/2024.emnlp-main.20/) · Fangkai Jiao, Chengwei Qin, Zhengyuan Liu, Nancy F. Chen, Shafiq Joty
  把推理当成规划来收集轨迹，并合成过程奖励，而不是只看最后答对没有。

### Best Special Theme Paper

* **DEM: Distribution Edited Model for Training with Mixed Data Distributions**
  [论文](https://aclanthology.org/2024.emnlp-main.1074) · Dhananjay Ram, Aditya Rawal, Momchil Hardalov, Nikolaos Pappas, Sheng Zha

### Best Resource Paper

* **KidLM: Advancing Language Models for Children – Early Insights and Future Directions**
  [论文](https://aclanthology.org/2024.emnlp-main.277) · Mir Tafseer Nayeem, Davood Rafiei

* **A User-Centric Multi-Intent Benchmark for Evaluating Large Language Models**
  [论文](https://aclanthology.org/2024.emnlp-main.210) · Jiayin Wang, Fengran Mo, Weizhi Ma, Peijie Sun, Min Zhang, Jian-Yun Nie

### Best Social Impact Paper

* **What the Harm? Quantifying the Tangible Impact of Gender Bias in Machine Translation with a Human-centered Study**
  [论文](https://aclanthology.org/2024.emnlp-main.1002) · Beatrice Savoldi, Sara Papi, Matteo Negri, Ana Guerberof-Arenas, Luisa Bentivogli

* **STOP! Benchmarking Large Language Models with Sensitivity Testing on Offensive Progressions**
  [论文](https://aclanthology.org/2024.emnlp-main.243) · Robert Morabito, Sangmitra Madhusudan, Tyler McDonald, Ali Emami

* **Twists, Humps, and Pebbles: Multilingual Speech Recognition Models Exhibit Gender Performance Gaps**
  [论文](https://aclanthology.org/2024.emnlp-main.1188/) · Giuseppe Attanasio, Beatrice Savoldi, Dennis Fucci, Dirk Hovy

## 2023

### Best Paper

* **Label Words are Anchors: An Information Flow Perspective for Understanding In-Context Learning**
  [论文](https://aclanthology.org/2023.emnlp-main.609) · Lean Wang, Lei Li, Damai Dai, Deli Chen, Hao Zhou, Fandong Meng, Jie Zhou, Xu Sun
  上下文学习里，标签词像锚，信息是从例子流到这些词上再流出来的。

* **Faster Minimum Bayes Risk Decoding with Confidence-based Pruning**
  [论文](https://aclanthology.org/2023.emnlp-main.767) · Julius Cheng, Andreas Vlachos

* **Ignore This Title and HackAPrompt: Exposing Systemic Vulnerabilities of LLMs Through a Global Prompt Hacking Competition**
  [论文](https://aclanthology.org/2023.emnlp-main.302) · Sander V Schulhoff, Jeremy Pinto, Anaum Khan, Louis-François Bouchard, Chenglei Si, Svetlina Anati 等
  用一场全球提示词比赛说明，注入漏洞是系统性的，不是几个越狱例子。

* **PaperMage: A Unified Toolkit for Processing, Representing, and Manipulating Visually-Rich Scientific Documents**
  [论文](https://aclanthology.org/2023.emnlp-demo.45) · _Kyle Lo, Zejiang Shen, Benjamin Newman, Joseph Chee Chang, Russell Authur, Erin Bransom 等

* **Personalized Dense Retrieval on Global Index for Voice-enabled Conversational Systems**
  [论文](https://aclanthology.org/2023.emnlp-industry.9) · Masha Belyi, Charlotte Dzialo, Chaitanya Dwivedi, Prajit Reddy Muppidi, Kanna Shimizu

### Outstanding Paper

* **LINC: A Neurosymbolic Approach for Logical Reasoning by Combining Language Models with First-Order Logic Provers**
  [论文](https://aclanthology.org/2023.emnlp-main.313) · Theo X. Olausson, Alex Gu, Ben Lipkin, Cedegao E. Zhang, Armando Solar-Lezama, Joshua B. Tenenbaum, Roger P. Levy

* **Toward a Critical Toponymy Framework for Named Entity Recognition: A Case Study of Airbnb in New York City**
  [论文](https://aclanthology.org/2023.emnlp-main.284) · Mikael Brunila, Jack LaViolette, Sky CH-Wang, Priyanka Verma, Clara Féré, Grant McKenzie

* **SODA: Million-scale Dialogue Distillation with Social Commonsense Contextualization**
  [论文](https://aclanthology.org/2023.emnlp-main.799) · Hyunwoo Kim, Jack Hessel, Liwei Jiang, Peter West, Ximing Lu, Youngjae Yu 等

* **Incorporating Worker Perspectives into MTurk Annotation Practices for NLP**
  [论文](https://aclanthology.org/2023.emnlp-main.64) · Olivia Huang, Eve Fleisig, Dan Klein

* **Physician Detection of Clinical Harm in Machine Translation: Quality Estimation Aids in Reliance and Backtranslation Identifies Critical Errors**
  [论文](https://aclanthology.org/2023.emnlp-main.712) · Nikita Mehandru, Sweta Agrawal, Yimin Xiao, Ge Gao, Elaine C Khoong, Marine Carpuat, Niloufar Salehi

* **Preserving Knowledge Invariance: Rethinking Robustness Evaluation of Open Information Extraction**
  [论文](https://aclanthology.org/2023.emnlp-main.360) · Ji Qi, Chuchun Zhang, Xiaozhi Wang, Kaisheng Zeng, Jifan Yu, Jinxin Liu 等

* **Is ChatGPT Good at Search? Investigating Large Language Models as Re-Ranking Agents**
  [论文](https://aclanthology.org/2023.emnlp-main.923) · Weiwei Sun, Lingyong Yan, Xinyu Ma, Shuaiqiang Wang, Pengjie Ren, Zhumin Chen, Dawei Yin, Zhaochun Ren

* **Unraveling Feature Extraction Mechanisms in Neural Networks**
  [论文](https://aclanthology.org/2023.emnlp-main.650) · Xiaobing Sun, Jiaxi Li, Wei Lu

* **ViPE: Visualise Pretty-much Everything**
  [论文](https://aclanthology.org/2023.emnlp-main.333) · Hassan Shahmohammadi, Adhiraj Ghosh, Hendrik Lensch

* **Revisiting the Optimality of Word Lengths**
  [论文](https://aclanthology.org/2023.emnlp-main.137) · Tiago Pimentel, Clara Meister, Ethan Wilcox, Kyle Mahowald, Ryan Cotterell

* **Language Model Quality Correlates with Psychometric Predictive Power in Multiple Languages**
  [论文](https://aclanthology.org/2023.emnlp-main.466) · Ethan Wilcox, Clara Meister, Ryan Cotterell, Tiago Pimentel

* **FedID: Federated Interactive Distillation for Large-Scale Pretraining Language Models**
  [论文](https://aclanthology.org/2023.emnlp-main.529) · Xinge Ma, Jiangming Liu, Jin Wang, Xuejie Zhang

* **Ties Matter: Meta-Evaluating Modern Metrics with Pairwise Accuracy and Tie Calibration**
  [论文](https://aclanthology.org/2023.emnlp-main.798) · Daniel Deutsch, George Foster, Markus Freitag

* **Cross-Lingual Consistency of Factual Knowledge in Multilingual Language Models**
  [论文](https://aclanthology.org/2023.emnlp-main.658) · Jirui Qi, Raquel Fernández, Arianna Bisazza

* **Look-back Decoding for Open-Ended Text Generation**
  [论文](https://aclanthology.org/2023.emnlp-main.66) · Nan Xu, Chunting Zhou, Asli Celikyilmaz, Xuezhe Ma

* **Text Embeddings Reveal (Almost) As Much As Text**
  [论文](https://aclanthology.org/2023.emnlp-main.765) · John Xavier Morris, Volodymyr Kuleshov, Vitaly Shmatikov, Alexander M Rush

* **Understanding Compositional Data Augmentation in Typologically Diverse Morphological Inflection**
  [论文](https://aclanthology.org/2023.emnlp-main.19) · Farhan Samir, Miikka Silfverberg

* **IfQA: A Dataset for Open-domain Question Answering under Counterfactual Presuppositions**
  [论文](https://aclanthology.org/2023.emnlp-main.515) · Wenhao Yu, Meng Jiang, Peter Clark, Ashish Sabharwal

* **Counter Turing Test (CT2): AI-Generated Text Detection is Not as Easy as You May Think - Introducing AI Detectability Index (ADI)**
  [论文](https://aclanthology.org/2023.emnlp-main.136) · Megha Chakraborty, S.M Towhidul Islam Tonmoy, S M Mehedi Zaman, Shreya Gautam, Tanay Kumar, Krish Sharma 等

* **Bridging Continuous and Discrete Spaces: Interpretable Sentence Representation Learning via Compositional Operations**
  [论文](https://aclanthology.org/2023.emnlp-main.900) · James Y. Huang, Wenlin Yao, Kaiqiang Song, Hongming Zhang, Muhao Chen, Dong Yu

* **The Sentiment Problem: A Critical Survey towards Deconstructing Sentiment Analysis**
  [论文](https://aclanthology.org/2023.emnlp-main.848) · Pranav Narayanan Venkit, Mukund Srinath, Sanjana Gautam, Saranya Venkatraman, Vipul Gupta, Rebecca J. Passonneau, Shomir Wilson

* **Homophone Disambiguation Reveals Patterns of Context Mixing in Speech Transformers**
  [论文](https://aclanthology.org/2023.emnlp-main.513) · Hosein Mohebbi, Grzegorz Chrupała, Willem Zuidema, Afra Alishahi

* **Background Summarization of Event Timelines**
  [论文](https://aclanthology.org/2023.emnlp-main.505) · Adithya Pratapa, Kevin Small, Markus Dreyer

* **Linear-Time Modeling of Linguistic Structure: An Order-Theoretic Perspective**
  [论文](https://aclanthology.org/2023.emnlp-main.52) · Tianyu Liu, Afra Amini, Mrinmaya Sachan, Ryan Cotterell

* **Joint Dialogue Topic Segmentation and Categorization: A Case Study on Clinical Spoken Conversations**
  [论文](https://aclanthology.org/2023.emnlp-industry.19) · Zhengyuan Liu, Siti Umairah Md Salleh, Hong Choon Oh, Pavitra Krishnaswamy, Nancy Chen

## 2022

这一年会后官网不稳定。下面两篇分别由康奈尔大学的新闻和短文第一作者的公开说明交叉核实，并与会后综述一致。若另有 Outstanding 名单，这里不猜测，标为待补充。

### Best Long Paper

* **Abstract Visual Reasoning with Tangram Shapes**
  [论文](https://aclanthology.org/2022.emnlp-main.38/) · Anya Ji, Noriyuki Kojima, Noah Rush, Alane Suhr, Wai Keen Vong, Robert Hawkins, Yoav Artzi
  用七巧板做抽象视觉推理资源，看多模态模型会不会只靠整体轮廓、而不懂部件。

### Best Short Paper

* **Topic-Regularized Authorship Representation Learning**
  [论文](https://aclanthology.org/2022.emnlp-main.70/) · Jitkapat Sawatphol, Nonthakit Chaiwong, Can Udomcharoenchaikit, Sarana Nutanong
  作者表征很容易偷用主题线索；这篇把主题从作者向量里压下去，才能谈跨主题的作者识别。

# NAACL

## 2026

该年未举办。章节站点列出的下一次会议是 NAACL 2027（旧金山）。

## 2025

### Best Paper

* **The BiGGen Bench: A Principled Benchmark for Fine-grained Evaluation of Language Models with Language Models \**
  [论文](https://aclanthology.org/2025.naacl-long.303) · Seungone Kim, Juyoung Suk, Ji Yong Cho, Shayne Longpre, Chaeeun Kim, Dongkeun Yoon 等

### Outstanding Paper

* **PeerQA: A Scientific Question Answering Dataset from Peer Reviews**
  [论文](https://aclanthology.org/2025.naacl-long.22) · Tim Baumgärtner, Ted Briscoe, Iryna Gurevych

* **Is your benchmark truly adversarial? AdvScore: Evaluating Human-Grounded Adversarialness**
  [论文](https://aclanthology.org/2025.naacl-long.27) · Yoo Yeon Sung, Maharshi Gor, Eve Fleisig, Ishani Mondal, Jordan Lee Boyd-Graber

* **NLI under the Microscope: What Atomic Hypothesis Decomposition Reveals**
  [论文](https://aclanthology.org/2025.naacl-long.130) · Neha Srikanth, Rachel Rudinger

* **IrokoBench: A New Benchmark for African Languages in the Age of Large Language Models**
  [论文](https://aclanthology.org/2025.naacl-long.139) · David Ifeoluwa Adelani, Jessica Ojo, Israel Abebe Azime, Jian Yun Zhuang, Jesujoba Oluwadara Alabi, Xuanli He 等

* **ACCORD: Closing the Commonsense Measurability Gap**
  [论文](https://aclanthology.org/2025.naacl-long.193) · François Roewer-Després, Jinyue Feng, Zining Zhu, Frank Rudzicz

* **DrawEduMath: Evaluating Vision Language Models with Expert-Annotated Students' Hand-Drawn Math Images**
  [论文](https://aclanthology.org/2025.naacl-long.352) · Sami Baral, Li Lucy, Ryan Knight, Alice Ng, Luca Soldaini, Neil Heffernan, Kyle Lo

* **A Logical Fallacy-Informed Framework for Argument Generation**
  [论文](https://aclanthology.org/2025.naacl-long.374) · Luca Mouchel, Debjit Paul, Shaobo Cui, Robert West, Antoine Bosselut, Boi Faltings

* **Learning vs Retrieval: The Role of In-Context Examples in Regression with Large Language Models**
  [论文](https://aclanthology.org/2025.naacl-long.417) · Aliakbar Nafar, K. Brent Venable, Parisa Kordjamshidi

* **Multi3Hate: Multimodal, Multilingual, and Multicultural Hate Speech Detection with Vision–Language Models**
  [论文](https://aclanthology.org/2025.naacl-long.490) · Minh Duc Bui, Katharina von der Wense, Anne Lauscher

* **How Good Are LLMs for Literary Translation, Really? Literary Translation Evaluation with Humans and LLMs**
  [论文](https://aclanthology.org/2025.naacl-long.548) · Ran Zhang, Wei Zhao, Steffen Eger

### Best Paper Runner-up

* **REL-A.I.: An Interaction-Centered Approach To Measuring Human-LM Reliance**
  [论文](https://aclanthology.org/2025.naacl-long.556/) · Kaitlyn Zhou, Jena D. Hwang, Xiang Ren, Nouha Dziri, Dan Jurafsky, Maarten Sap
  人有多依赖模型，要在交互过程里量，而不是问一句你信不信它。

### Best Social Impact Paper

* **FLEURS-ASL: Including American Sign Language in Massively Multilingual Multitask Evaluation**
  [论文](https://aclanthology.org/2025.naacl-long.314) · Garrett Tanzer

### Best Theme Paper

* **WorldCuisines: A Massive-Scale Benchmark for Multilingual and Multicultural Visual Question Answering on Global Cuisines**
  [论文](https://aclanthology.org/2025.naacl-long.167) · Genta Indra Winata, Frederikus Hudi, Patrick Amadeus Irawan, David Anugraha, Rifki Afina Putri, WANG YUTONG 等

### Best Theme Paper Runner-up

* **Developing multilingual speech synthesis system for Ojibwe, Mi'kmaq, and Maliseet**
  [论文](https://aclanthology.org/2025.naacl-short.69) · Shenran Wang, Changbing Yang, Michael l parkhill, Chad Quinn, Christopher Hammerly, Jian Zhu

## 2024

### Best Paper

* **Visual Grounding Helps Learn Word Meanings in Low-Data Regimes**
  [论文](https://aclanthology.org/2024.naacl-long.71) · Chengxu Zhuang, Evelina Fedorenko, Jacob Andreas
  词义在数据很少时，视觉落地比再堆文本更有用。

* **Evaluating the Deductive Competence of Large Language Models**
  [论文](https://aclanthology.org/2024.naacl-long.476) · S. M. Seals, Valerie Shalin
  演绎能力和考试分数不是一回事，要把推理步骤单独拿出来评。

### Outstanding Paper

* **LM-Infinite: Zero-Shot Extreme Length Generalization for Large Language Models**
  [论文](https://aclanthology.org/2024.naacl-long.222) · Chi Han, Qifan Wang, Hao Peng, Wenhan Xiong, Yu Chen, Heng Ji, Sinong Wang
  不继续训练，也想让模型在远超训练长度的输入上还能用。

* **Defining and Detecting Vulnerability in Human Evaluation Guidelines: A Preliminary Study Towards Reliable NLG Evaluation**
  [论文](https://aclanthology.org/2024.naacl-long.441/) · Jie Ruan, Wenqing Wang, Xiaojun Wan
  人工评测指南本身会有漏洞，指南不可靠时，评测结果也不可靠。

* **Unlocking Emergent Modularity in Large Language Models**
  [论文](https://aclanthology.org/2024.naacl-long.144) · Zihan Qiu, Zeyu Huang, Jie Fu
  大模型里的模块化不一定要预先设计，有可能从训练里长出来。

* **R-Tuning: Instructing Large Language Models to Say `I Don't Know'**
  [论文](https://aclanthology.org/2024.naacl-long.394/) · Hanning Zhang, Shizhe Diao, Yong Lin, Yi Fung, Qing Lian, Xingyao Wang 等
  让模型学会拒答，本身可以作为指令微调的目标，而不是只在推理时加一句提示。

* **Teaching Language Models to Self-Improve through Interactive Demonstrations**
  [论文](https://aclanthology.org/2024.naacl-long.287) · Xiao Yu, Baolin Peng, Michel Galley, Jianfeng Gao, Zhou Yu
  小模型的自我改进不是提示出来的，要靠它和更强模型交互、再重放自己的修正。

* **A Pretrainer's Guide to Training Data: Measuring the Effects of Data Age, Domain Coverage, Quality, & Toxicity**
  [论文](https://aclanthology.org/2024.naacl-long.179) · Shayne Longpre, Gregory Yauney, Emily Reif, Katherine Lee, Adam Roberts, Barret Zoph 等
  预训练数据的年龄、领域、质量和毒性要分开量，不能合成一个干净分数。

### Best Resource Paper

* **Exploring Cross-Cultural Differences in English Hate Speech Annotations: From Dataset Construction to Analysis**
  [论文](https://aclanthology.org/2024.naacl-long.236) · Nayeon Lee, Chani Jung, Junho Myung, Jiho Jin, Jose Camacho-Collados, Juho Kim, Alice Oh
  同一句英语算不算仇恨，不同文化的标注者并不一致，数据集必须把这个差异留下来。

### Best Social Impact Paper

* **Understanding the Capabilities and Limitations of Large Language Models for Cultural Commonsense**
  [论文](https://aclanthology.org/2024.naacl-long.316) · Siqi Shen, Lajanugen Logeswaran, Moontae Lee, Honglak Lee, Soujanya Poria, Rada Mihalcea
  文化常识不是英语常识的翻译，模型的能力和限度要按文化来写。

### Best Theme Paper

* **Grammar-based Data Augmentation for Low-Resource Languages: The Case of Guarani-Spanish Neural Machine Translation**
  [论文](https://aclanthology.org/2024.naacl-long.354/) · Agustín Lucas, Alexis Baladón, Victoria Pardiñas, Marvin M. Agüero-Torales, Santiago Góngora, Luis Chiruzzo
  低资源翻译的增广可以用语法来做，而不是只回译。

## 2023

该年未举办。2023 年在北美召开的是 ACL（多伦多），NAACL 按惯例停办。

## 2022

### Honorable Mention

* **A Balanced Data Approach for Evaluating Cross-Lingual Transfer: Mapping the Linguistic Blood Bank**
  [论文](https://aclanthology.org/2022.naacl-main.361/) · Dan Malkin, Tomasz Limisiewicz, Gabriel Stanovsky
  跨语言迁移的评测数据本身可能不平衡，先把语言覆盖画清楚。

* **NewsEdits: A News Article Revision Dataset and a Novel Document-Level Reasoning Challenge**
  [论文](https://aclanthology.org/2022.naacl-main.10/) · Alexander Spangher, Xiang Ren, Jonathan May, Nanyun Peng
  新闻的修改历史是文档级推理的资源，不只是另一份摘要数据。

### Honorable Mention (human-centered NLP)

* **Automatic Correction of Human Translations**
  [论文](https://aclanthology.org/2022.naacl-main.36/) · Jessy Lin, Geza Kovacs, Aditya Shastry, Joern Wuebker, John DeNero
  同一篇同时拿到新任务/新资源奖，以及以人为中心主题的荣誉提名。

### Best Paper (new task)

* **FRUIT: Faithfully Reflecting Updated Information in Text**
  [论文](https://aclanthology.org/2022.naacl-main.269) · Robert L. Logan IV, Alexandre Tachard Passos, Sameer Singh, Ming-Wei Chang
  文本里的事实会过期，更新文本是和纠错不同的任务。

### Best Paper (new method)

* **NeuroLogic A*esque Decoding: Constrained Text Generation with Lookahead Heuristics**
  [论文](https://aclanthology.org/2022.naacl-main.57) · Ximing Lu, Sean Welleck, Peter West, Liwei Jiang, Jungo Kasai, Daniel Khashabi 等
  带约束的生成是搜索问题，向前看一步的启发式比生成完再过滤更接近解码本身。

### Best Paper (human-centered NLP)

* **User-Driven Research of Medical Note Generation Software**
  [论文](https://aclanthology.org/2022.naacl-main.29) · Tom Knoll, Francesco Moramarco, Alex Papadopoulos Korfiatis, Rachel Young, Claudia Ruffini, Mark Perera 等
  病历生成该怎么做，要让真正写病历的人参与定义，而不是只优化摘要分数。

### Best Paper (efficient NLP)

* **FNet: Mixing Tokens with Fourier Transforms**
  [论文](https://aclanthology.org/2022.naacl-main.319/) · James Lee-Thorp, Joshua Ainslie, Ilya Eckstein, Santiago Ontanon
  用无参数的傅里叶变换代替自注意力来混合 token，追问注意力是不是唯一的混合方式。

### Best Paper (new task and new resource)

* **Automatic Correction of Human Translations**
  [论文](https://aclanthology.org/2022.naacl-main.36) · Jessy Lin, Geza Kovacs, Aditya Shastry, Joern Wuebker, John DeNero
  改的是人的译文，不是机器译文；任务、数据和译员一起定义。

# AAAI

## 2026

### Outstanding Paper

* **Model Change for Description Logic Concepts**
  [论文](https://arxiv.org/abs/2603.05562) · Ana Ozaki, Jandson S. Ribeiro
  研究描述逻辑概念在知识变化时如何更新。

* **Causal Structure Learning for Dynamical Systems with Theoretical Score Analysis**
  [论文](https://doi.org/10.1609/aaai.v40i43.40999) · Nicholas Tagliapietra, Katharina Ensinger, Christoph Zimmer, Osman Mian
  为动力系统学习因果结构，并给出得分函数的理论分析。

* **ReconVLA: Reconstructive Vision-Language-Action Model as Effective Robot Perceiver**
  [论文](https://arxiv.org/abs/2508.10333) · Wenxuan Song, Ziyang Zhou, Han Zhao, Jiayi Chen, Pengxiang Ding, Haodong Yan 等
  用重建式的视觉-语言-动作模型作为机器人的感知器，让动作学习服务于把场景重建对。

* **High-Pass Matters: Theoretical Insights and Sheaflet-Based Design for Hypergraph Neural Networks**
  [论文](https://doi.org/10.1609/aaai.v40i27.39469) · Ming Li, Yujie Fang, Dongrui Shen, Han Feng, Xiaosheng Zhuang, Kelin Xia, Pietro Liò
  从高通过滤解释超图网络，并用 sheaflet 设计对应的结构。

* **LLM2CLIP: Powerful Language Model Unlocks Richer Cross-Modality Representation**
  [论文](https://arxiv.org/abs/2411.04997) · Weiquan Huang, Aoqi Wu, Yifan Yang, Xufang Luo, Yuqing Yang, Usman Naseem 等
  用更强的大语言模型替换 CLIP 里较弱的文本塔，以得到更丰富的跨模态表示。

### Best Paper, AI for Social Impact

* **PlantTraitNet: An Uncertainty-Aware Multimodal Framework for Global-Scale Plant Trait Inference from Citizen Science Data**
  [论文](https://arxiv.org/abs/2511.06943) · Ayushi Sharma, Johanna Trost, Daniel Lusk, Johannes Dollinger, Julian Schrader, Christian Rossi 等
  用带不确定性的多模态模型，从公民科学数据推断全球尺度的植物性状。

* **Generalizable Slum Detection from Satellite Imagery with Mixture-of-Experts**
  [论文](https://doi.org/10.1609/aaai.v40i45.41227) · Sumin Lee, Sungwon Park, Jeasurk Yang, Jihee Kim, Meeyoung Cha
  用专家混合从卫星图检测不同国家的非正式住区，使检测能跨城市泛化。

### Best Paper, AI Alignment

* **On the Alignment of Large Language Models with Global Human Opinion**
  [论文](https://doi.org/10.1609/aaai.v40i44.41102) · Yang Liu, Masahiro Kaneko, Chenhui Chu
  考察大语言模型和全球范围内人类意见的对齐程度，而不是只和单一文化的偏好数据对齐。

## 2025

### Outstanding Paper

* **Every Bit Helps: Achieving the Optimal Distortion with a Few Queries**
  [论文](https://doi.org/10.1609/aaai.v39i13.33507) · Soroush Ebadian, Nisarg Shah
  证明只需少量查询就能在一定投票设定下达到最优扭曲度。

* **Efficient Rectification of Neuro-Symbolic Reasoning Inconsistencies by Abductive Reflection**
  [论文](https://arxiv.org/abs/2412.08457) · Wen-Chao Hu, Wang-Zhou Dai, Yuan Jiang, Zhi-Hua Zhou
  用反绎反思修正神经符号推理中的不一致，而不是整段重推。

* **Revelations: A Decidable Class of POMDPs with Omega-Regular Objectives**
  [论文](https://arxiv.org/abs/2412.12063) · Marius Belly, Nathanaël Fijalkow, Hugo Gimbert, Florian Horn, Guillermo A. Pérez, Pierre Vandenhove
  划出一类带 ω-正则目标的部分可观测马尔可夫决策过程，使验证和求解可判定。

### Outstanding Paper, AI for Social Alignment

* **DivShift: Exploring Domain-Specific Distribution Shifts in Large-Scale, Volunteer-Collected Biodiversity Datasets**
  [论文](https://arxiv.org/abs/2410.19816) · Elena Sierra, Lauren Gillespie, Salim Soltani, Moises Exposito-Alonso, Teja Kattenborn
  分析志愿者采集的大规模生物多样性数据里，特定域的分布偏移从哪来。

## 2024

### Outstanding Paper

* **GxVAEs: Two Joint VAEs Generate Hit Molecules from Gene Expression Profiles**
  [论文](https://ojs.aaai.org/index.php/AAAI/article/view/29248) · Chen Li, Yoshihiro Yamanishi
  用一对联合变分自编码器，从基因表达谱生成候选活性分子。

* **Reliable Conflictive Multi-view Learning**
  [论文](https://arxiv.org/abs/2402.16897) · Cai Xu, Jiajun Si, Ziyu Guan, Wei Zhao, Yue Wu, Xiyue Gao
  在视图之间互相冲突时仍可靠地学习，而不是默认视图只是同一事实的不同侧面。

* **Proportional Aggregation of Preferences for Sequential Decision Making**
  [论文](https://arxiv.org/abs/2306.14858) · Nikhil Chandak, Shashwat Goel, Dominik Peters
  把比例代表式的偏好聚合扩展到序贯决策，使少数偏好不会在每一步都被吃掉。

### Best Student Paper, AI for Social Impact

* **Scaling Up Pareto Optimization for Tree Structures with Affine Transformations: Evaluating Hybrid Floating Solar-Hydropower Systems in the Amazon**
  [论文](https://ojs.aaai.org/index.php/AAAI/article/view/30210) · Marc Grimson, Rafael Almeida, Qinru Shi, Yiwei Bai, Hector Angarita, Felipe Siqueira Pacheco 等
  把树上的帕累托优化放大，用来评估亚马逊水电与漂浮光伏的混合方案。

### Best Paper, AI for Social Impact

* **DISCount: Counting in Large Image Collections with Detector-Based Importance Sampling**
  [论文](https://arxiv.org/abs/2306.03151) · Gustavo Perez, Subhransu Maji, Daniel Sheldon
  用检测器做重要性采样，在大规模图像集合里估计物体数量，而不必看完每一张。

### Best Paper Honorable Mention, AI for Social Impact

* **Nowcasting Temporal Trends Using Indirect Surveys**
  [论文](https://arxiv.org/abs/2307.06643) · Ajitesh Srivastava, Juan Marcos Ramirez, Sergio Díaz, Jose Aguilar, Antonio Fernández Anta, Antonio Ortega, Rosa Lillo
  用间接调查而非直接提问来临近预报时间趋势。

### Best Student Paper Honorable Mention, AI for Social Impact

* **Arbitrariness and Social Prediction: The Confounding Role of Variance in Fair Classification**
  [论文](https://ojs.aaai.org/index.php/AAAI/article/view/30203) · A. Feder Cooper, Katherine Lee, Madiha Choksi, Solon Barocas, Christopher De Sa, James Grimmelmann 等
  授奖页用的是 Is My Prediction Arbitrary；proceedings 标题是这一条。公平榜上的胜负如果经不起重复训练，就不该写成结论。

## 2023

### Outstanding Paper

* **Misspecification in Inverse Reinforcement Learning**
  [论文](https://arxiv.org/abs/2212.03201) · Joar Skalse, Alessandro Abate
  刻画奖励函数设错时，逆强化学习会恢复出什么样的策略和奖励。

### Outstanding Student Paper

* **Decorate the Newcomers: Visual Domain Prompt for Continual Test Time Adaptation**
  [论文](https://arxiv.org/abs/2212.04145) · Yulu Gan, Yan Bai, Yihang Lou, Xianzhe Ma, Renrui Zhang, Nian Shi, Lin Luo
  用视觉域提示让模型在持续到来的新测试域上适应，同时少忘旧域。

### Distinguished Paper

* **DropMessage: Unifying Random Dropping for Graph Neural Networks**
  [论文](https://arxiv.org/abs/2204.10037) · Taoran Fang, Zhiqing Xiao, Chunping Wang, Jiarong Xu, Xuan Yang, Yang Yang
  把图神经网络里各种随机丢弃统一成对消息的丢弃。

* **Two Heads are Better than One: Image-Point Cloud Network for Depth-Based 3D Hand Pose Estimation**
  [论文](https://doi.org/10.1609/aaai.v37i2.25310) · Pengfei Ren, Yuchen Chen, Jiachang Hao, Haifeng Sun, Qi Qi, Jingyu Wang, Jianxin Liao
  同时使用深度图和点云估计三维手部姿态。

* **Neural Architecture Search for Wide Spectrum Adversarial Robustness**
  [论文](https://doi.org/10.1609/aaai.v37i1.25118) · Zhi Cheng, Yanxi Li, Minjing Dong, Xiu Su, Shan You, Chang Xu
  用神经架构搜索寻找在多种攻击强度下都较稳健的结构，而不是只对一种扰动半径稳健。

* **CowClip: Reducing CTR Prediction Model Training Time from 12 hours to 10 minutes on 1 GPU**
  [论文](https://arxiv.org/abs/2204.06240) · Zangwei Zheng, Pengtai Xu, Xuan Zou, Da Tang, Zhen Li, Chenguang Xi 等
  用自适应裁剪稳定点击率模型的大批量训练，把单卡训练时间从以小时计降到以分钟计。

* **DICNet: Deep Instance-Level Contrastive Network for Double Incomplete Multi-View Multi-Label Classification**
  [论文](https://arxiv.org/abs/2303.08358) · Chengliang Liu, Jie Wen, Xiaoling Luo, Chao Huang, Zhihao Wu, Yong Xu
  处理视图和标签同时缺失的多视图多标签分类。

* **Exploring Tuning Characteristics of Ventral Stream’s Neurons for Few-Shot Image Classification**
  [论文](https://doi.org/10.1609/aaai.v37i1.25128) · Lintao Dong, Wei Zhai, Zheng-Jun Zha
  借用腹侧视觉通路神经元的调谐特性来做少样本图像分类。

* **MaskBooster: End-to-End Self-Training for Sparsely Supervised Instance Segmentation**
  [论文](https://doi.org/10.1609/aaai.v37i3.25481) · Shida Zheng, Chenshu Chen, Xi Yang, Wenming Tan
  在掩码标注很稀时用自训练把实例分割做成端到端学习。

* **SimFair: A Unified Framework for Fairness-Aware Multi-Label Classification**
  [论文](https://arxiv.org/abs/2302.09683) · Tianci Liu, Haoyu Wang, Yaqing Wang, Xiaoqian Wang, Lu Su, Jing Gao
  为多标签分类提供一个统一的公平性框架。

* **XRand: Differentially Private Defense against Explanation-Guided Attacks**
  [论文](https://arxiv.org/abs/2212.04454) · Truc Nguyen, Phung Lai, Hai Phan, My T. Thai
  用差分隐私扰动解释，防御根据解释反推或攻击模型的方法。

* **Clustering What Matters: Optimal Approximation for Clustering with Outliers**
  [论文](https://arxiv.org/abs/2212.00696) · Akanksha Agrawal, Tanmay Inamdar, Saket Saurabh, Jie Xue
  给带离群点的聚类一个最优近似算法。

* **Robust Average-Reward Markov Decision Processes**
  [论文](https://arxiv.org/abs/2301.00858) · Yue Wang, Alvaro Velasquez, George Atia, Ashley Prater-Bennette, Shaofeng Zou
  研究平均奖励准则下的鲁棒马尔可夫决策过程。

* **Efficient Answer Enumeration in Description Logics with Functional Roles**
  [论文](https://arxiv.org/abs/2211.15248) · Carsten Lutz, Marcin Przybylko
  在带函数角色的描述逻辑里高效枚举查询答案。

## 2022

### Outstanding Paper

* **Online Certification of Preference-based Fairness for Personalized Recommender Systems**
  [论文](https://arxiv.org/abs/2104.14527) · Virginie Do, Sam Corbett-Davies, Jamal Atif, Nicolas Usunier
  给个性化推荐一个在线证书，说明基于偏好的公平约束是否被满足。

### Outstanding Paper Honorable Mention

* **Bayesian Persuasion in Sequential Decision-Making**
  [论文](https://arxiv.org/abs/2106.05137) · Jiarui Gan, Rupak Majumdar, Goran Radanovic, Adish Singla
  把贝叶斯劝说放进序贯决策，研究信息发送方如何在多步互动里披露信息。

* **Operator-Potential Heuristics for Symbolic Search**
  [论文](https://doi.org/10.1609/aaai.v36i9.21210) · Daniel Fišer, Álvaro Torralba, Jörg Hoffmann
  为符号搜索设计基于算子势的启发式，改进规划里的符号可达性分析。

### Outstanding Student Paper Honorable Mention

* **Compilation of Aggregates in ASP Systems**
  [论文](https://doi.org/10.1609/aaai.v36i5.20527) · Giuseppe Mazzotta, Francesco Ricca, Carmine Dodaro
  改进答案集编程系统里聚合约束的编译方式。

* **Entropy Estimation via Normalizing Flow**
  [论文](https://doi.org/10.1609/aaai.v36i9.21237) · Ziqiao Ao, Jinglai Li
  用归一化流估计分布的熵。

### Outstanding Student Paper

* **InfoLM: A New Metric to Evaluate Summarization & Data2Text Generation**
  [论文](https://arxiv.org/abs/2112.01589) · Pierre Colombo, Chloé Clavel, Pablo Piantanida
  用预训练语言模型上的信息度量评估摘要和数据到文本，而不是只比较表面 n 元重叠。

### Distinguished Paper

* **AlphaHoldem: High-Performance Artificial Intelligence for Heads-Up No-Limit Poker via End-to-End Reinforcement Learning**
  [论文](https://doi.org/10.1609/aaai.v36i4.20394) · Enmin Zhao, Renye Yan, Jinqiu Li, Kai Li, Junliang Xing
  用端到端强化学习训练两人无限注德州扑克智能体。

* **Certified Symmetry and Dominance Breaking for Combinatorial Optimisation**
  [论文](https://doi.org/10.1609/aaai.v36i4.20283) · Bart Bogaerts, Stephan Gocht, Ciaran McCreesh, Jakob Nordström
  给对称性和支配关系的破除提供可检验的证书，避免搜索被等价分支拖死。

* **Online Elicitation of Necessarily Optimal Matchings**
  [论文](https://arxiv.org/abs/2112.04227) · Jannik Peters
  在线询问偏好，直到能够确定一个必然最优的匹配。

* **Sampling-Based Robust Control of Autonomous Systems with Non-Gaussian Noise**
  [论文](https://arxiv.org/abs/2110.12662) · Thom Badings, Alessandro Abate, Nils Jansen, David Parker, Hasan Poonawala, Marielle Stoelinga
  为非高斯噪声下的自治系统做基于采样的鲁棒控制。

* **Subset Approximation of Pareto Regions with Bi-objective A***
  [论文](https://doi.org/10.1609/aaai.v36i9.21276) · Jorge Baier, Carlos Hernández, Nicolás Rivera
  用双目标 A* 近似帕累托前沿的一个子集，而不是试图枚举整个前沿。

* **The SoftCumulative Constraint with Quadratic Penalty**
  [论文](https://doi.org/10.1609/aaai.v36i4.20296) · Yanick Ouellet, Claude-Guy Quimper
  给软累积约束配上二次罚，使资源超限可以被连续地惩罚而不是直接判不可行。

## 时间检验奖

原论文早于 2022，是后来的会议回看约十年前的工作。不放进上面各年的研究地图。

* **Toward an Architecture for Never-Ending Language Learning**（AAAI Classic Paper Award，2025 年颁发，原论文 2010）
  [论文](https://ojs.aaai.org/index.php/AAAI/article/view/7519) · Andrew Carlson, Justin Betteridge, Bryan Kisiel, Burr Settles, Estevam Hruschka, Tom Mitchell
  NELL 把语言学习写成一个不停读网页、不停改信念的系统，而不是一次训练结束。

* **Maximum Entropy Inverse Reinforcement Learning**（AAAI Classic Paper Award，2024 年颁发，原论文 2008）
  [论文](https://cdn.aaai.org/AAAI/2008/AAAI08-227.pdf) · Brian D. Ziebart, Andrew Maas, J. Andrew Bagnell, Anind K. Dey
  最大熵逆强化学习让演示对应一整族策略，而不是一条唯一轨迹。

* **Theta*: Any-Angle Path Planning on Grids**（AAAI Classic Paper Award，2023 年颁发，原论文 2007）
  [论文](https://cdn.aaai.org/AAAI/2007/AAAI07-187.pdf) · Alex Nash, Kenny Daniel, Sven Koenig, Ariel Felner
  在网格上找任意角度的路径，不必先被格子的边绑死。

* **Winning the DARPA Grand Challenge with an AI Robot**（AAAI Classic Paper Award，2022 年颁发，原论文 2006）
  [论文](https://www.aaai.org/Papers/AAAI/2006/AAAI06-154.pdf) · Michael Montemerlo, Sebastian Thrun, Hendrik Dahlkamp, David Stavens, Sven Strohband
  沙漠挑战赛的系统论文：感知、规划和控制要在一辆车上同时成立。

* **Corpus-Based and Knowledge-Based Measures of Text Semantic Similarity**（AAAI Classic Paper Honorable Mention，2022 年颁发，原论文 2006）
  [论文](https://cdn.aaai.org/AAAI/2006/AAAI06-123.pdf) · Rada Mihalcea, Courtney Corley, Carlo Strapparava
  语义相似度可以同时用语料共现和知识库，不必二选一。

# 还没写上的

- **NeurIPS 2026**：待补充。
- **NAACL 2023、NAACL 2026**：该年未举办。
- **EMNLP 2022** 除最佳长文、最佳短文以外的 Outstanding 名单：待补充。
- **ACL 2023** 的授奖页写明 Outstanding Paper 有 39 篇。下面收进 38 篇。剩下的一篇在页面上标题和作者粘在同一行，没有可靠拆开，不单列，避免把标题写错。
- 条目里写着「链接待补充」的，是标题和奖项已经核对，但没有找到稳定的论文页。ACL 2025 的 *Typology-Guided Adaptation for African NLP* 属于这一类。
