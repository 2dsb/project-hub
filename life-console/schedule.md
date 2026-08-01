---
active: true
period: "Summer Break (2026-06-23 ~ 2026-08-18)"
energy_peak: "14:00-22:00"
note: "Gaokao completed 06-07. PKU admitted. University starts 08-18. Full days free."
blocks:
  # ===== Summer — Every Day =====
  - id: summer-morning
    title: "Morning"
    day_of_week: null
    start_time: "08:00"
    end_time: "12:00"
    type: recurring
    date: null
    project_slug: null
    note: "Light tasks, reading, review, English practice"

  - id: summer-afternoon
    title: "Deep Work I"
    day_of_week: null
    start_time: "14:00"
    end_time: "17:00"
    type: recurring
    date: null
    project_slug: null
    note: "Energy peak — primary project work"

  - id: summer-evening
    title: "Deep Work II"
    day_of_week: null
    start_time: "19:00"
    end_time: "20:30"
    type: recurring
    date: null
    project_slug: null
    note: "Secondary projects, execution, light cognitive work. Hard cutoff 20:30 — studying past this wrecks sleep (see deep-work-recovery-cycle)."

  - id: summer-wind-down
    title: "Wind-Down"
    day_of_week: null
    start_time: "21:00"
    end_time: "23:00"
    type: recurring
    date: null
    project_slug: null
    note: "Recreational only — games, videos, light reading. No cognitive work. Protects sleep and prevents recovery gaps."

  # ===== PKU Admission Deadlines =====
  - id: pku-apply-info
    title: "核对并填写新生信息"
    day_of_week: null
    start_time: "09:00"
    end_time: "10:00"
    type: once
    date: 2026-07-23
    project_slug: pku-freshman-prep
    note: "apply.pku.edu.cn/freshman 核对并填写相关信息"

  - id: pku-yanyuan-aid
    title: "燕园关爱助学金申请"
    day_of_week: null
    start_time: "09:00"
    end_time: "10:00"
    type: once
    date: 2026-08-04
    project_slug: pku-freshman-prep
    note: "apply.pku.edu.cn/freshman 提交助学金申请"

  - id: pku-bedding-payment
    title: "床上用品采购付款"
    day_of_week: null
    start_time: "09:00"
    end_time: "09:30"
    type: once
    date: 2026-08-08
    project_slug: pku-freshman-prep
    note: "扫码付款（如需学校采购），见《关于购买学生公寓床上用品的通知》"

  - id: pku-uniform
    title: "领取军训服装"
    day_of_week: null
    start_time: "09:00"
    end_time: "10:00"
    type: once
    date: 2026-08-10
    project_slug: pku-freshman-prep
    note: "apply.pku.edu.cn/freshman 领取军训服装"

  - id: pku-activate-account
    title: "激活北大账号 + 绑定手机"
    day_of_week: null
    start_time: "09:00"
    end_time: "10:00"
    type: once
    date: 2026-08-13
    project_slug: pku-freshman-prep
    note: "https://portal.pku.edu.cn 激活账号，绑定个人手机号（出入校权限 8/18 生效）"

  - id: pku-bank-deposit
    title: "农行卡存入学费 ≥7000 元"
    day_of_week: null
    start_time: "09:00"
    end_time: "09:30"
    type: once
    date: 2026-08-15
    project_slug: pku-freshman-prep
    note: "农行卡扣款缴费，或 http://cwpay.pku.edu.cn 网上缴费（学号+8位生日密码）"

  - id: pku-rules-exam
    title: "校规校纪考试"
    day_of_week: null
    start_time: "08:00"
    end_time: "12:00"
    type: once
    date: 2026-08-17
    project_slug: pku-freshman-prep
    note: "http://fresh.pku.edu.cn → 报到前准备 → 校纪校规考试（学号+8位生日密码）"

  - id: pku-shuttle-register
    title: "抵京班车需求登记"
    day_of_week: null
    start_time: "14:00"
    end_time: "14:30"
    type: once
    date: 2026-08-17
    project_slug: pku-freshman-prep
    note: "http://fresh.pku.edu.cn → 报到前准备 → 抵京后乘班车到校需求登记（17:00 截止）"

  - id: pku-checkin
    title: "🎓 北京大学报到"
    day_of_week: null
    start_time: "08:00"
    end_time: "17:00"
    type: once
    date: 2026-08-18
    project_slug: pku-freshman-prep
    note: "携带《录取通知书》+ 一寸照片10张，校本部迎新接待站报到 → 领宿舍钥匙 → 楼长办公室登记入住"

  - id: pku-insurance
    title: "学生团体保险投保"
    day_of_week: null
    start_time: "09:00"
    end_time: "09:30"
    type: once
    date: 2026-08-31
    project_slug: pku-freshman-prep
    note: "登录个人门户完成投保程序，《关于2026级新生参加学生团体保险项目的通知》"

  - id: pku-scholarship
    title: "新生奖学金申请"
    day_of_week: null
    start_time: "09:00"
    end_time: "10:00"
    type: once
    date: 2026-09-07
    project_slug: pku-freshman-prep
    note: "apply.pku.edu.cn/freshman 新生奖学金申请"

  - id: pku-archive-submit
    title: "高中学籍档案提交"
    day_of_week: null
    start_time: "09:00"
    end_time: "10:00"
    type: once
    date: 2026-09-01
    project_slug: pku-freshman-prep
    note: "报到后两周内，密封档案交至院系学工办公室"
---

# 日程定义

## Summer Break (06-23 ~ 08-18)

Gaokao completed. Full days available until university starts August 18.

| Block | Time | Type |
|-------|------|------|
| Morning | 08:00-12:00 | Light — reading, review, English, low-intensity tasks |
| Deep Work I | 14:00-17:00 | Heavy — primary project focus (energy peak) |
| Deep Work II | 19:00-20:30 | Medium — secondary projects, execution, light cognitive work |
| Wind-Down | 21:00-23:00 | Recreational only — games, videos, light reading |

**Hard cutoff rule**: No cognitive work after 20:30. Studying close to bedtime → cognitive arousal → poor sleep → multi-day recovery gap. See [[deep-work-recovery-cycle]].

## Pre-Gaokao School Schedule (archived)

The high school timetable (Monday-Friday classes, Sunday self-study) was active until 2026-06-07. Preserved in git history — commit `d8c919a` and earlier.
