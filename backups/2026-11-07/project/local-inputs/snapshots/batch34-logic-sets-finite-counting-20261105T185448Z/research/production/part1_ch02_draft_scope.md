> **历史记录（de08a8a及之前）**：下文描述当时稿件与验收方案，不是本轮最终状态。当前修订、来源缺口及验收结论以 `part1_revision_disposition.md` 和 `part1_acceptance.json` 为准；原样记录已归档 `history/de08a8a/`。

# 第2章00Bxx草稿范围与接入说明

日期：2026-11-05。撰写代理：/root/part1_chapter2。状态：可审校草稿；未自行授予独立审阅、构建、视觉验收或完成状态。

## 实际范围

已新建第2章正文和独立答案，保留00Bxx原10叶、全书第24—33节；全G，未提高为T/S。正文9253字符（含Markdown），答案2526字符；初估正文10—14页，实际以构建为准。章首列目标、路线、先修、采用约定、排除范围与篇幅；十节分别处理摘要、一般/专题汇编、一般/专题会议论文集、纪念文集、一般/专题译文集、重印及其他类目。

A—E是明示虚构的同一文章传播材料，作者、年份、页码均为教学给定，不对应真实学术成果，不含伪DOI、ISBN或许可。正文不展示/声称证明模拟文章的研究结论。新增6道原创阅读核验练习及独立详解，覆盖证据边界、引用身份、版本更正、量词、混合载体和独立证明/许可区别。

## 不重复与边界

充分阅读第一章后，仅回链其定义/前提/证明、书目以及量词区别，不重写集合与方程教学。题2-4给出独立原创的二人二书完整反例。分类计数、标题、原归属均从本地台账核对；未改任何台账、构建代码或其他稿件，未提交或推送。

## 来源核验

- C2-S1：本地data/msc_taxonomy.json和data/production/sections.json逐项核对。原始PDF及抽取全文未复制进新稿。

- C2-S2：Crossref官方仓库api_format.md，本次公开读取成功（10677字节），SHA-256：70aa9d3fc20bbf8d2f4d35e756f40e65e8e1ebaaecec2eaf1e6e1098996ed5c1。文件版本表最新v3，2018-05-15。实际读到Work、Contributor、Update、License等字段定义。

- 同仓库README.md实际读取45347字节，SHA-256：7c1d9010cacd833645f7019ea6a8825b70fb3f33b5db98907c5d0637eec4663a，首页明确deprecated；正文已如实说明，只用作历史元数据结构例证，不宣称现行API核验，不依此编造真实文章记录。

- 两文件公开URL分别为https://raw.githubusercontent.com/CrossRef/rest-api-doc/master/api_format.md 与https://raw.githubusercontent.com/CrossRef/rest-api-doc/master/README.md。未复制源全文进入分发稿；来源可读、来源时效、数学正确性与转载许可分开。

- 当前网络策略未列AMS/zbMATH/Crossref服务域，未绕过策略；没有声称本轮成功访问那些服务。一次公开arXiv文档路径尝试返回404，未将其列为来源。

## 自检与待审

本章+第一章组合的全部内部锚点链接均能定位，无重复锚点；十个节号/代码/中文标题与当前分类台账逐项一致；6题与6答案双向链接齐全。独立数学审阅、教学审阅、PDF/离线HTML/ZIP构建和逐页查看由其他代理接续；本文件不把自检等同独立验收。

## 稿件身份

- `manuscript/review_ch02/chapter.md`：SHA-256 `6ec66043da26980d6300e470a3ac53f8a76d4cb896a6f7533bfb9bbca3a466ac`。

- `manuscript/review_ch02/answers.md`：SHA-256 `2813b876dfe34be9d57e03c5e23cc1b7b6ac6b8f271cd0e676b7c2c49d81acee`。


## 十节精确范围计划接口

以下JSON可并入父代理的scope_plan.sections；正文作者身份应包含`/root/part1_chapter2`。reference_entries共同指向本章已核验且标明时效的来源段，不要求每个文献类型虚构一篇真实代表论文。

```json

[
  {
    "code": "00B05",
    "parent_code": "00Bxx",
    "depth": "G",
    "body_source": "manuscript/review_ch02/chapter.md",
    "anchor": "sec-00B05",
    "objectives": [
      {
        "id": "00B05-1",
        "text": "辨认讲座摘要的信息边界，由报告人和题名寻找全文而不宣称已读证明"
      }
    ],
    "prerequisites": [
      "manuscript/review_ch01/chapter.md#sec-00A05",
      "manuscript/review_ch01/chapter.md#sec-00A15"
    ],
    "adopted_rules": [
      "通常书目描述约定；所给格式仅作可核对记录示范"
    ],
    "excluded_topics": [
      "完整论文证明",
      "报告人与完整作者名单的未经核验等同"
    ],
    "reference_entries": [
      "manuscript/review_ch02/chapter.md#ch02-sources"
    ],
    "exercise_answer_pairs": [
      {
        "question": "manuscript/review_ch02/chapter.md#ch02-question-01",
        "answer": "manuscript/review_ch02/answers.md#ch02-answer-01"
      }
    ]
  },
  {
    "code": "00B10",
    "parent_code": "00Bxx",
    "depth": "G",
    "body_source": "manuscript/review_ch02/chapter.md",
    "anchor": "sec-00B10",
    "objectives": [
      {
        "id": "00B10-1",
        "text": "区分单篇文章与汇编载体，分别记录作者、编者和使用位置"
      }
    ],
    "prerequisites": [
      "manuscript/review_ch01/chapter.md#sec-00A15",
      "manuscript/review_ch02/chapter.md#sec-00B05"
    ],
    "adopted_rules": [
      "通常书目描述约定；所给格式仅作可核对记录示范"
    ],
    "excluded_topics": [
      "统一规定所有引文格式",
      "把广泛主题解释成全称数学结论"
    ],
    "reference_entries": [
      "manuscript/review_ch02/chapter.md#ch02-sources"
    ],
    "exercise_answer_pairs": [
      {
        "question": "manuscript/review_ch02/chapter.md#ch02-question-02",
        "answer": "manuscript/review_ch02/answers.md#ch02-answer-02"
      }
    ]
  },
  {
    "code": "00B15",
    "parent_code": "00Bxx",
    "depth": "G",
    "body_source": "manuscript/review_ch02/chapter.md",
    "anchor": "sec-00B15",
    "objectives": [
      {
        "id": "00B15-1",
        "text": "从专题目录选择具体问题并记录不同文章的定义和先修条件"
      }
    ],
    "prerequisites": [
      "manuscript/review_ch01/chapter.md#sec-00A05",
      "manuscript/review_ch01/chapter.md#sec-00A15"
    ],
    "adopted_rules": [
      "通常书目描述约定；所给格式仅作可核对记录示范"
    ],
    "excluded_topics": [
      "任何具体专题的深层数学理论",
      "因同册出版而默认术语相同"
    ],
    "reference_entries": [
      "manuscript/review_ch02/chapter.md#ch02-sources"
    ],
    "exercise_answer_pairs": [
      {
        "question": "manuscript/review_ch02/chapter.md#ch02-question-05",
        "answer": "manuscript/review_ch02/answers.md#ch02-answer-05"
      }
    ]
  },
  {
    "code": "00B20",
    "parent_code": "00Bxx",
    "depth": "G",
    "body_source": "manuscript/review_ch02/chapter.md",
    "anchor": "sec-00B20",
    "objectives": [
      {
        "id": "00B20-1",
        "text": "区分会议日期、出版日期与单篇定位，分开核验发表身份和论证内容"
      }
    ],
    "prerequisites": [
      "manuscript/review_ch01/chapter.md#sec-00A15",
      "manuscript/review_ch02/chapter.md#sec-00B05"
    ],
    "adopted_rules": [
      "通常书目描述约定；所给格式仅作可核对记录示范"
    ],
    "excluded_topics": [
      "保证同行评议状态",
      "将DOI或ISBN当作数学正确性证明"
    ],
    "reference_entries": [
      "manuscript/review_ch02/chapter.md#ch02-sources"
    ],
    "exercise_answer_pairs": [
      {
        "question": "manuscript/review_ch02/chapter.md#ch02-question-01",
        "answer": "manuscript/review_ch02/answers.md#ch02-answer-01"
      },
      {
        "question": "manuscript/review_ch02/chapter.md#ch02-question-02",
        "answer": "manuscript/review_ch02/answers.md#ch02-answer-02"
      }
    ]
  },
  {
    "code": "00B25",
    "parent_code": "00Bxx",
    "depth": "G",
    "body_source": "manuscript/review_ch02/chapter.md",
    "anchor": "sec-00B25",
    "objectives": [
      {
        "id": "00B25-1",
        "text": "追踪专题文章的具体引用链，逐项检查适用条件并辨认无起点的循环引用"
      }
    ],
    "prerequisites": [
      "manuscript/review_ch01/chapter.md#sec-00A05",
      "manuscript/review_ch02/chapter.md#sec-00B15"
    ],
    "adopted_rules": [
      "通常书目描述约定；所给格式仅作可核对记录示范"
    ],
    "excluded_topics": [
      "证明特定专题的研究结论",
      "把相互引用一概判为循环论证"
    ],
    "reference_entries": [
      "manuscript/review_ch02/chapter.md#ch02-sources"
    ],
    "exercise_answer_pairs": [
      {
        "question": "manuscript/review_ch02/chapter.md#ch02-question-06",
        "answer": "manuscript/review_ch02/answers.md#ch02-answer-06"
      }
    ]
  },
  {
    "code": "00B30",
    "parent_code": "00Bxx",
    "depth": "G",
    "body_source": "manuscript/review_ch02/chapter.md",
    "anchor": "sec-00B30",
    "objectives": [
      {
        "id": "00B30-1",
        "text": "区分纪念文集的回忆、历史评价与研究主张并选择相应证据"
      }
    ],
    "prerequisites": [
      "manuscript/review_ch01/chapter.md#sec-00A05",
      "manuscript/review_ch01/chapter.md#sec-00A15"
    ],
    "adopted_rules": [
      "通常书目描述约定；所给格式仅作可核对记录示范"
    ],
    "excluded_topics": [
      "裁定真实成果优先权",
      "人物生平的完整考证"
    ],
    "reference_entries": [
      "manuscript/review_ch02/chapter.md#ch02-sources"
    ],
    "exercise_answer_pairs": [
      {
        "question": "manuscript/review_ch02/chapter.md#ch02-question-05",
        "answer": "manuscript/review_ch02/answers.md#ch02-answer-05"
      }
    ]
  },
  {
    "code": "00B50",
    "parent_code": "00Bxx",
    "depth": "G",
    "body_source": "manuscript/review_ch02/chapter.md",
    "anchor": "sec-00B50",
    "objectives": [
      {
        "id": "00B50-1",
        "text": "记录原作者、译者与译文所据版本，核对更正和量词顺序"
      }
    ],
    "prerequisites": [
      "manuscript/review_ch01/chapter.md#sec-00A30",
      "manuscript/review_ch02/chapter.md#sec-00B05"
    ],
    "adopted_rules": [
      "通常书目描述约定；所给格式仅作可核对记录示范"
    ],
    "excluded_topics": [
      "保证译文全部准确",
      "从免费可读推断转载许可"
    ],
    "reference_entries": [
      "manuscript/review_ch02/chapter.md#ch02-sources"
    ],
    "exercise_answer_pairs": [
      {
        "question": "manuscript/review_ch02/chapter.md#ch02-question-03",
        "answer": "manuscript/review_ch02/answers.md#ch02-answer-03"
      },
      {
        "question": "manuscript/review_ch02/chapter.md#ch02-question-04",
        "answer": "manuscript/review_ch02/answers.md#ch02-answer-04"
      }
    ]
  },
  {
    "code": "00B55",
    "parent_code": "00Bxx",
    "depth": "G",
    "body_source": "manuscript/review_ch02/chapter.md",
    "anchor": "sec-00B55",
    "objectives": [
      {
        "id": "00B55-1",
        "text": "对照专题译文的术语、定义与版本，明确数学先修和翻译核验边界"
      }
    ],
    "prerequisites": [
      "manuscript/review_ch01/chapter.md#sec-00A05",
      "manuscript/review_ch02/chapter.md#sec-00B15",
      "manuscript/review_ch02/chapter.md#sec-00B50"
    ],
    "adopted_rules": [
      "通常书目描述约定；所给格式仅作可核对记录示范"
    ],
    "excluded_topics": [
      "系统教授专业术语或外语",
      "未经原文核验而补造原词"
    ],
    "reference_entries": [
      "manuscript/review_ch02/chapter.md#ch02-sources"
    ],
    "exercise_answer_pairs": [
      {
        "question": "manuscript/review_ch02/chapter.md#ch02-question-03",
        "answer": "manuscript/review_ch02/answers.md#ch02-answer-03"
      },
      {
        "question": "manuscript/review_ch02/chapter.md#ch02-question-04",
        "answer": "manuscript/review_ch02/answers.md#ch02-answer-04"
      }
    ]
  },
  {
    "code": "00B60",
    "parent_code": "00Bxx",
    "depth": "G",
    "body_source": "manuscript/review_ch02/chapter.md",
    "anchor": "sec-00B60",
    "objectives": [
      {
        "id": "00B60-1",
        "text": "区分原发、重印与修订，核对分页和更正并识别同源传播"
      }
    ],
    "prerequisites": [
      "manuscript/review_ch01/chapter.md#sec-00A15",
      "manuscript/review_ch02/chapter.md#sec-00B05"
    ],
    "adopted_rules": [
      "通常书目描述约定；所给格式仅作可核对记录示范"
    ],
    "excluded_topics": [
      "据重印次数认定独立证明",
      "授予外文献再分发许可"
    ],
    "reference_entries": [
      "manuscript/review_ch02/chapter.md#ch02-sources"
    ],
    "exercise_answer_pairs": [
      {
        "question": "manuscript/review_ch02/chapter.md#ch02-question-06",
        "answer": "manuscript/review_ch02/answers.md#ch02-answer-06"
      }
    ]
  },
  {
    "code": "00B99",
    "parent_code": "00Bxx",
    "depth": "G",
    "body_source": "manuscript/review_ch02/chapter.md",
    "anchor": "sec-00B99",
    "objectives": [
      {
        "id": "00B99-1",
        "text": "综合生成文章核验卡并明确未知项，描述混合材料而不滥用其他类目"
      }
    ],
    "prerequisites": [
      "manuscript/review_ch02/chapter.md#sec-00B05",
      "manuscript/review_ch02/chapter.md#sec-00B20",
      "manuscript/review_ch02/chapter.md#sec-00B50",
      "manuscript/review_ch02/chapter.md#sec-00B60"
    ],
    "adopted_rules": [
      "通常书目描述约定；所给格式仅作可核对记录示范"
    ],
    "excluded_topics": [
      "专业编目规则的完备体系",
      "凭卡片核验虚构全文证明"
    ],
    "reference_entries": [
      "manuscript/review_ch02/chapter.md#ch02-sources"
    ],
    "exercise_answer_pairs": [
      {
        "question": "manuscript/review_ch02/chapter.md#ch02-question-01",
        "answer": "manuscript/review_ch02/answers.md#ch02-answer-01"
      },
      {
        "question": "manuscript/review_ch02/chapter.md#ch02-question-02",
        "answer": "manuscript/review_ch02/answers.md#ch02-answer-02"
      },
      {
        "question": "manuscript/review_ch02/chapter.md#ch02-question-03",
        "answer": "manuscript/review_ch02/answers.md#ch02-answer-03"
      },
      {
        "question": "manuscript/review_ch02/chapter.md#ch02-question-05",
        "answer": "manuscript/review_ch02/answers.md#ch02-answer-05"
      },
      {
        "question": "manuscript/review_ch02/chapter.md#ch02-question-06",
        "answer": "manuscript/review_ch02/answers.md#ch02-answer-06"
      }
    ]
  }
]

```
