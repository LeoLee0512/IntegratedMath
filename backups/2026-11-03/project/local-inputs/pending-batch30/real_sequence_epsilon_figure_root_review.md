# 第30批数列图：主编独立代码与图像核验

审阅者/root。实际全文阅读完整独立脚本与制作报告，并实际打开候选PNG：上下误差带、零线、n=3空心边界点和n=4实心入带点及两个箭头清楚，图底不等式与最早阈值说明完整；未见文字覆盖、裁切或缺字。未将有限画布代替全尾量词证明。

对任意自然n≥4，既有自然嵌入保序与正倒数反序给0<1/(ν(n)+1)≤1/5<1/4。n=3是每个N≤3的尾部失败见证，因此4确为最早严格阈值。图公式中的n须由正文明确为嵌入后的实数简写，指标仍为自然数。正负误差带用于|b_n−0|<ε，并非只画单侧条件；所有数值值在脚本中先以Fraction精确表示，float只服务绘图。

本次独立加载作者脚本，在新的/tmp输出目录重新运行；全部精确断言通过，候选与复现PNG文件字节及Pillow解码像素完全相同。实际Python/Matplotlib环境一致，不声称跨环境压缩字节一致。脚本仅检查所画15项，任意尾项推理由上面的数学论证给出，任意ε的收敛证明仍由正文负责。

本报告不属于制作作者自审，未核尚未冻结的正文图注，也未查看本批正式PDF；完整函数附录、正式渲染字号与页面仍待核验。

- `/tmp/draw_real_sequence_epsilon.py`：`3f3c84d5b74024510af609abbf4037ae8cf27afe3a27f2625359eb548c117b74`
- `/tmp/real-sequence-epsilon-figure/b2_real_sequence_epsilon.png`：`9bf05e1f447c9ec0e0c55a5253b4ea7c16a9a632cc514e09c22d9d8287cfabc0`
- `/tmp/real-sequence-root-repro/b2_real_sequence_epsilon.png`：`9bf05e1f447c9ec0e0c55a5253b4ea7c16a9a632cc514e09c22d9d8287cfabc0`
