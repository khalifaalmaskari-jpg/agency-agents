# 🏢 70 Business Specialists for Claude — Free & Open Source

> **An entire AI team for your business. One install. No subscription — because it's free.**
>
> Your social media manager, copywriter, strategist, sales coach, analyst, HR lead — and 64 more. Each specialist is pre-configured with expert-level instructions: open it, ask your question, get expert output. Set up in under 10 minutes.

This pack is a curated selection of 70 business specialists from [The Agency](../../README.md)'s full roster, organized the way a real company is: by department. It covers every business function — marketing, sales, ops, finance, HR, legal, strategy, support — so there's one specialist for every part of your business.

Commercial products sell this exact promise for $97+. This pack is the open-source equivalent: same job-to-be-done, fully inspectable prompts, community-maintained, MIT licensed.

---

## ⚡ Setup in under 10 minutes

**Claude Code / Claude Desktop (as subagents):**

```bash
git clone https://github.com/msitarzewski/agency-agents.git
cd agency-agents
./scripts/install.sh --tool claude-code --agents-file packs/70-business-specialists/agents.txt
```

That's it. Every specialist is now available as a subagent — mention the one you need ("ask the Conversion Copywriter to rewrite this landing page") or let Claude route to them.

**Claude.ai (as Projects):** create a Project per specialist you use often, and paste the agent file's contents into the Project's custom instructions. Start with your top 5 — most people live in Copywriter, Social Media Strategist, Sales Coach, Executive Assistant, and Financial Analyst.

**Any other tool:** each specialist is a plain Markdown system prompt. Copy, paste, done. (`./scripts/install.sh --list tools` shows all supported formats.)

**Make it sound like you (do this first):** run the **[Business Onboarding Interviewer](../../specialized/business-onboarding-interviewer.md)**. It asks you short rounds of questions about your business — nothing is assumed, so it works for any business, and you can run it once per business you operate — then writes a `business-context.md` brief.

**Make it automatic:** copy [`CLAUDE.md.template`](CLAUDE.md.template) into your working folder as `CLAUDE.md` (or paste it into your claude.ai Project instructions). Claude reads it at the start of every session, so every specialist automatically reads your `business-context.md`, matches your voice, and uses your region's conventions — no pasting required.

**Don't know who to ask?** Talk to the **[Front Desk Router](../../specialized/front-desk-router.md)** 🛎️ — describe any problem in plain words and it names the right specialist(s), the order to use them in, and gives you a paste-ready prompt for each.

---

## 👥 Meet your team — 70 specialists across 11 departments

### 📣 Marketing & Content (12)
| Specialist | What they do for you |
|---|---|
| [Social Media Strategist](../../marketing/marketing-social-media-strategist.md) | Platform strategy, content calendars, engagement plans |
| [Content Creator](../../marketing/marketing-content-creator.md) | Blog posts, articles, multi-format content |
| [Conversion Copywriter](../../marketing/marketing-conversion-copywriter.md) | Ads, landing pages, and emails that sell |
| [Email Marketing Strategist](../../marketing/marketing-email-strategist.md) | Sequences, follow-ups, deliverability |
| [SEO Specialist](../../marketing/marketing-seo-specialist.md) | Rankings, keyword strategy, technical SEO |
| [Growth Hacker](../../marketing/marketing-growth-hacker.md) | Experiments, loops, and channels that compound |
| [PR & Communications Manager](../../marketing/marketing-pr-communications-manager.md) | Press releases, announcements, crisis comms |
| [LinkedIn Content Creator](../../marketing/marketing-linkedin-content-creator.md) | Authority-building posts and profiles |
| [Instagram Curator](../../marketing/marketing-instagram-curator.md) | Visual feed strategy, Reels, Stories |
| [TikTok Strategist](../../marketing/marketing-tiktok-strategist.md) | Short-video hooks and virality mechanics |
| [Reddit Community Builder](../../marketing/marketing-reddit-community-builder.md) | Community presence without getting banned |
| [Podcast Strategist](../../marketing/marketing-podcast-strategist.md) | Show strategy, episodes, guesting |

### 💰 Paid Advertising (5)
| Specialist | What they do for you |
|---|---|
| [PPC Campaign Strategist](../../paid-media/paid-media-ppc-strategist.md) | Google/search campaigns end to end |
| [Paid Social Strategist](../../paid-media/paid-media-paid-social-strategist.md) | Meta, TikTok, LinkedIn ad strategy |
| [Ad Creative Strategist](../../paid-media/paid-media-creative-strategist.md) | Creative concepts and iteration systems |
| [Paid Media Auditor](../../paid-media/paid-media-auditor.md) | Finds wasted spend in your accounts |
| [Tracking & Measurement Specialist](../../paid-media/paid-media-tracking-specialist.md) | Pixels, conversions, attribution |

### 🤝 Sales (9)
| Specialist | What they do for you |
|---|---|
| [Sales Coach](../../sales/sales-coach.md) | Call reviews, scripts, objection handling |
| [Outbound Strategist](../../sales/sales-outbound-strategist.md) | Cold email and outbound sequences |
| [Deal Strategist](../../sales/sales-deal-strategist.md) | Win plans for deals in flight |
| [Discovery Coach](../../sales/sales-discovery-coach.md) | Better discovery calls, better qualification |
| [Pipeline Analyst](../../sales/sales-pipeline-analyst.md) | Forecasting and funnel health |
| [Proposal Strategist](../../sales/sales-proposal-strategist.md) | Proposals that close |
| [Account Strategist](../../sales/sales-account-strategist.md) | Expansion and key-account planning |
| [Offer & Lead Gen Strategist](../../sales/sales-offer-lead-gen-strategist.md) | Offers and lead magnets that convert |
| [Sales Outreach](../../specialized/sales-outreach.md) | Personalized outreach at scale |

### 💬 Customer Success & Support (4)
| Specialist | What they do for you |
|---|---|
| [Customer Service](../../specialized/customer-service.md) | Support replies with empathy and policy |
| [Customer Success Manager](../../specialized/customer-success-manager.md) | Onboarding, retention, renewals |
| [Support Responder](../../support/support-support-responder.md) | Ticket triage and response drafting |
| [Language Translator](../../specialized/language-translator.md) | Serve customers in any language |

### ⚙️ Operations & Admin (7)
| Specialist | What they do for you |
|---|---|
| [Operations Manager](../../specialized/operations-manager.md) | SOPs, workflows, process fixes |
| [Workflow Architect](../../specialized/specialized-workflow-architect.md) | Automation and system design |
| [Chief of Staff](../../specialized/specialized-chief-of-staff.md) | Priorities, cadences, decision support |
| [Executive Assistant](../../specialized/executive-assistant.md) | Inbox triage, calendar defense, follow-ups |
| [Project Shepherd](../../project-management/project-management-project-shepherd.md) | Keeps projects moving and unblocked |
| [Meeting Notes Specialist](../../project-management/project-management-meeting-notes-specialist.md) | Notes, decisions, action items |
| [Document Generator](../../specialized/specialized-document-generator.md) | Polished docs from rough inputs |

### 📊 Finance (7)
| Specialist | What they do for you |
|---|---|
| [Chief Financial Officer](../../specialized/chief-financial-officer.md) | Strategic finance for non-finance founders |
| [Bookkeeper & Controller](../../finance/finance-bookkeeper-controller.md) | Clean books, month-end close |
| [Financial Analyst](../../finance/finance-financial-analyst.md) | Models, metrics, unit economics |
| [FP&A Analyst](../../finance/finance-fpa-analyst.md) | Budgets, forecasts, variance |
| [Tax Strategist](../../finance/finance-tax-strategist.md) | Tax planning (with CPA review) |
| [Pricing Analyst](../../specialized/specialized-pricing-analyst.md) | Pricing and packaging decisions |
| [Accounts Payable Agent](../../specialized/accounts-payable-agent.md) | Invoices, bills, payment runs |

### 🧑‍🤝‍🧑 HR & People (6)
| Specialist | What they do for you |
|---|---|
| [HR People Operations Lead](../../specialized/hr-people-operations-lead.md) | Policies, reviews, comp, hard conversations |
| [Recruitment Specialist](../../specialized/recruitment-specialist.md) | Job posts, sourcing, interview loops |
| [HR Onboarding](../../specialized/hr-onboarding.md) | First-day-to-first-year experience |
| [Corporate Training Designer](../../specialized/corporate-training-designer.md) | Training programs that stick |
| [Organizational Psychologist](../../specialized/organizational-psychologist.md) | Team dynamics and motivation |
| [Change Management Consultant](../../specialized/change-management-consultant.md) | Rollouts people don't revolt against |

### 🧭 Strategy & Research (7)
| Specialist | What they do for you |
|---|---|
| [Business Strategist](../../specialized/business-strategist.md) | Growth plans and strategic choices |
| [Competitive Intelligence Analyst](../../specialized/competitive-intelligence-analyst.md) | Competitor teardowns and battlecards |
| [Trend Researcher](../../product/product-trend-researcher.md) | Market trends before they're obvious |
| [Product Manager](../../product/product-manager.md) | Roadmaps and product decisions |
| [Feedback Synthesizer](../../product/product-feedback-synthesizer.md) | Customer feedback into priorities |
| [Investment Researcher](../../finance/finance-investment-researcher.md) | Deep research on markets and companies |
| [M&A Integration Manager](../../specialized/ma-integration-manager.md) | Acquisitions that actually integrate |

### ⚖️ Legal & Compliance (5)
| Specialist | What they do for you |
|---|---|
| [Legal Document Review](../../specialized/legal-document-review.md) | Contract review prep (with counsel) |
| [Legal Client Intake](../../specialized/legal-client-intake.md) | Intake and matter organization |
| [Legal Compliance Checker](../../support/support-legal-compliance-checker.md) | Policy and regulation checks |
| [Data Privacy Officer](../../specialized/data-privacy-officer.md) | GDPR/CCPA and data handling |
| [Grant Writer](../../specialized/grant-writer.md) | Grants and funding applications |

### 🎨 Brand & Design (5)
| Specialist | What they do for you |
|---|---|
| [Brand Guardian](../../design/design-brand-guardian.md) | Consistent brand voice and identity |
| [UI Designer](../../design/design-ui-designer.md) | Interfaces and design decisions |
| [UX Researcher](../../design/design-ux-researcher.md) | User research and usability |
| [Visual Storyteller](../../design/design-visual-storyteller.md) | Decks, infographics, visual narrative |
| [Image Prompt Engineer](../../design/design-image-prompt-engineer.md) | AI image generation that matches brand |

### 📈 Reporting & Analytics (3)
| Specialist | What they do for you |
|---|---|
| [Analytics Reporter](../../support/support-analytics-reporter.md) | Metrics into readable reports |
| [Executive Summary Generator](../../support/support-executive-summary-generator.md) | Anything into a one-page brief |
| [Data Consolidation Agent](../../specialized/data-consolidation-agent.md) | Messy data from many sources, unified |

---

## 🧩 Local Business Add-ons (16)

Beyond the core 70 — built for running a real business day to day. All included in `agents.txt`.

| Specialist | What they do for you |
|---|---|
| [Business Onboarding Interviewer](../../specialized/business-onboarding-interviewer.md) 🎤 | **Run first** — interviews you, writes the `business-context.md` every agent reads |
| [Front Desk Router](../../specialized/front-desk-router.md) 🛎️ | Describe any problem — get routed to the right specialist(s) with paste-ready prompts |
| [WhatsApp Business Specialist](../../marketing/marketing-whatsapp-business-specialist.md) | WhatsApp-first sales/support flows, broadcasts, Business API |
| [Reviews & Reputation Manager](../../marketing/marketing-reviews-reputation-manager.md) | Review responses, ratings recovery, review generation done legally |
| [Local SEO Specialist](../../marketing/marketing-local-seo-specialist.md) | Google Business Profile, local pack, "near me" visibility |
| [Influencer & UGC Manager](../../marketing/marketing-influencer-ugc-manager.md) | Creator partnerships, vetting, usage rights, disclosure |
| [E-commerce Store Operator](../../marketing/marketing-ecommerce-store-operator.md) | Shopify/WooCommerce/Amazon (incl. .ae/.sa, Noon), PDP conversion, cart recovery |
| [Webinar & Events Marketer](../../marketing/marketing-webinar-events-marketer.md) | Webinars, trade shows (GITEX/LEAP-aware), follow-up funnels |
| [Accounts Receivable & Collections](../../finance/finance-accounts-receivable-collections.md) | Getting paid: invoicing discipline, aging, dunning sequences |
| [Procurement & Vendor Negotiator](../../specialized/procurement-vendor-negotiator.md) | Buyer-side: quote comparison, SaaS renewals, contract red flags |
| [Partnerships & Affiliate Manager](../../sales/sales-partnerships-affiliate-manager.md) | Referral/affiliate programs, commission design, partner recruitment |
| [Pitch Deck & Fundraising Strategist](../../specialized/pitch-deck-fundraising-strategist.md) | Deck narrative, investor targeting, data rooms |
| [Retail Store Operations Manager](../../specialized/retail-store-operations-manager.md) 🏪 | Floor operations: rotas, cash discipline, store-health scorecards |
| [Logistics & Last-Mile Strategist](../../specialized/logistics-last-mile-strategist.md) 🛵 | Courier scorecards, COD reconciliation, delivery-promise design |
| [Insurance & Risk Manager](../../specialized/insurance-risk-manager.md) ☂️ | Risk registers, coverage gaps, claims readiness — incl. UAE mandatory covers |
| [Franchise Operations Advisor](../../specialized/franchise-operations-advisor.md) 🎡 | Buying a franchise or franchising your business — both sides, GCC-aware |

## 🕌 UAE, GCC & MENA Add-ons (9)

Region-focused specialists for businesses operating in the Gulf. All included in `agents.txt`.

| Specialist | What they do for you |
|---|---|
| [GCC & MENA Market Navigator](../../specialized/gcc-mena-market-navigator.md) 🦅 | Market entry & localization — per-country dialects, Ramadan/Eid calendars, payment landscape |
| [UAE & GCC Payroll Specialist](../../finance/finance-uae-gcc-payroll-specialist.md) 🧾 | WPS runs, EOSB/gratuity math, GPSSA/GOSI, DIFC/ADGM differences |
| [UAE Business Law Navigator](../../specialized/uae-business-law-navigator.md) 🐪 | Mainland vs. free zone, labour law prep, compliance calendars — routes to counsel |
| [Government Tender & Bid Writer](../../specialized/government-tender-bid-writer.md) 🏆 | Public tenders: compliance matrices, bid/no-bid, ICV/local content |
| [AI Governance Officer (UAE & GCC)](../../specialized/uae-ai-governance-officer.md) 🧿 | Responsible AI adoption: policies, risk registers, PDPL/DIFC Reg 10 awareness |
| [UAE Cybersecurity Compliance Specialist](../../security/security-uae-cybersecurity-compliance.md) 🇦🇪 | The regulator map: Cybersecurity Council, DESC ISR, ADHICS, CBUAE, PDPL gap assessments |
| [OT Security Engineer](../../security/security-ot-security-engineer.md) 🛢️ | Defending ICS/SCADA & plants: IEC 62443, segmentation, vendor remote access |
| [KSA Business Navigator](../../specialized/ksa-business-navigator.md) 🏜️ | Operating in Saudi: MISA, Nitaqat, ZATCA/FATOORAH, GOSI, Qiwa/Etimad platform map |
| [Arabic Copywriter](../../marketing/marketing-arabic-copywriter.md) 🖋️ | Native Arabic copy — MSA vs. Gulf dialect, transcreation not translation, RTL flags |

## 🏛️ Corporate & Group Add-ons (8)

For holding companies and groups of companies. All included in `agents.txt`. Run the Interviewer's **group mode** first — it writes the `group-context.md` these specialists read.

| Specialist | What they do for you |
|---|---|
| [Corporate Governance & Board Secretary](../../specialized/corporate-governance-board-secretary.md) 🗳️ | Board packs, resolutions, DoA matrices, subsidiary governance, RPT logging |
| [Group Financial Controller](../../finance/finance-group-financial-controller.md) 🧮 | Consolidation, intercompany reconciliation, IFRS, UAE Corporate Tax group & transfer pricing flags |
| [Internal Auditor](../../specialized/internal-auditor.md) 🔦 | Risk-based audit plans, controls testing, findings that actually get closed |
| [Treasury & Cash Manager](../../finance/finance-treasury-cash-manager.md) 💧 | Group cash visibility, 13-week forecasts, facilities/covenants, guarantees & LCs |
| [Enterprise Risk Manager](../../specialized/enterprise-risk-manager.md) ⚠️ | Group risk register, risk appetite, aggregation across entities, board heat maps |
| [Family Business & Succession Advisor](../../specialized/family-business-succession-advisor.md) 🌳 | Family charters, next-gen entry rules, succession & bus plans — Gulf family-group reality |
| [Revalidation Gatekeeper](../../specialized/revalidation-gatekeeper.md) 🚦 | The final gate before the chairman: source audits, hallucination hunts, PASS or RETURN — no rubber stamps |
| [Business Continuity Manager](../../specialized/business-continuity-manager.md) 🧯 | BCM: business impact analysis, RTO/RPO, crisis action cards, exercises — untested plans reported as unproven |

## 👔 Executive Chiefs & IT (9)

Dedicated chief seats for the org structure — each runs a department of specialists, reviews their output before the gate, and owns the function's numbers. The CFO seat is held by the [Chief Financial Officer](../../specialized/chief-financial-officer.md), already listed under Finance.

| Specialist | What they do for you |
|---|---|
| [Chief Marketing Officer](../../specialized/chief-marketing-officer.md) 📢 | Marketing & Branding: budget allocation, brand architecture, channel kill/scale decisions |
| [Chief Revenue Officer](../../specialized/chief-revenue-officer.md) 💹 | The revenue engine: pipeline discipline, forecast accuracy, discount authority, churn ownership |
| [Chief Operating Officer](../../specialized/chief-operating-officer.md) 🧰 | Delivery: capacity before commitments, operating cadence, SOP coverage, SLAs as measured |
| [Chief Human Resources Officer](../../specialized/chief-human-resources-officer.md) 👥 | People: workforce planning, comp band governance, non-family succession |
| [Chief Strategy Officer](../../specialized/chief-strategy-officer.md) 🛤️ | Strategy cycle, portfolio view on CFO actuals, kill criteria on every initiative, M&A funnel |
| [General Counsel](../../specialized/general-counsel.md) 🔏 | Legal function coordination and counsel management — never legal advice itself |
| [Chief Information Security Officer](../../specialized/chief-information-security-officer.md) 🏰 | Security program, honest RAG reporting, 60-minute incident escalation, defensive only |
| [Chief Information Officer](../../specialized/chief-information-officer.md) 💾 | The IT seat: systems landscape, buy-vs-build, SaaS audits, tested backups |
| [IT Service Manager](../../engineering/engineering-it-service-manager.md) | The IT department: service desk, incidents, ITIL discipline — reports to the CIO |

## 🕵️ Independent Audit Function (3 + Internal Auditor)

Reports to the chairman/audit committee only — never to the CEO line it audits. The [Internal Auditor](../../specialized/internal-auditor.md) (listed under Corporate & Group) works inside this function.

| Specialist | What they do for you |
|---|---|
| [Chief Audit Executive](../../specialized/chief-audit-executive.md) 🕵️ | Leads the function: risk-based audit plan, committee reporting, retested-closure regime, audit committee charter |
| [Fraud Examiner](../../specialized/fraud-examiner.md) 🪤 | Fraud prevention & detection: scheme catalog, small-data analytics, evidence-first investigations, counsel-gated actions |
| [IT Auditor](../../specialized/it-auditor.md) 🗝️ | Independently verifies the CIO's and CISO's controls: access, change, tested restores, in-system segregation of duties |

## 🏗️ Digital Build Unit (8)

App, website, and digital product building — under the CIO. All included in `agents.txt`.

| Specialist | What they do for you |
|---|---|
| [Frontend Developer](../../engineering/engineering-frontend-developer.md) | Websites and web apps — React/modern frontend |
| [Backend Architect](../../engineering/engineering-backend-architect.md) | APIs, databases, server architecture |
| [Mobile App Builder](../../engineering/engineering-mobile-app-builder.md) | iOS/Android apps |
| [Rapid Prototyper](../../engineering/engineering-rapid-prototyper.md) | MVPs and prototypes in days, not months |
| [CMS Developer](../../engineering/engineering-cms-developer.md) | WordPress and content-managed sites |
| [DevOps Automator](../../engineering/engineering-devops-automator.md) | Hosting, deployment, CI/CD |
| [UX Architect](../../design/design-ux-architect.md) | Information architecture and user flows before pixels |
| [AI Engineer](../../engineering/engineering-ai-engineer.md) | AI features inside your products |

## ☁️ IT Architecture & Cloud (5)

The IT landscape layer and cloud/platform experts — under the CIO. All included in `agents.txt`. (ITIL 4 is covered by the [IT Service Manager](../../engineering/engineering-it-service-manager.md) above.)

| Specialist | What they do for you |
|---|---|
| [Enterprise IT Architect](../../engineering/engineering-enterprise-it-architect.md) 🏙️ | The whole-landscape layer: capability maps, portfolio dispositions, integration rules, ADRs |
| [Azure Cloud Architect](../../engineering/engineering-azure-cloud-architect.md) ⛅ | Landing zones, Entra ID/hybrid AD, cost governance, UAE/KSA region awareness |
| [AWS Cloud Architect](../../engineering/engineering-aws-cloud-architect.md) 🪣 | Multi-account Organizations, IAM, Well-Architected reviews, cost engineering |
| [Microsoft 365 & Copilot Specialist](../../engineering/engineering-m365-copilot-specialist.md) 🧑‍✈️ | Tenant hygiene, licensing math, and Copilot readiness-before-licenses deployment |
| [Full-Stack Developer](../../engineering/engineering-full-stack-developer.md) 🥞 | End-to-end vertical slices: schema → API → UI → deploy, no handoffs |

---

## 🎁 The "bonus sprints" — free equivalents

Paid bundles throw in training upsells. The open ecosystem already has them:

| Paid bonus | Free equivalent |
|---|---|
| "Master Claude Cowork" | [Anthropic Academy — Claude for Work](https://www.anthropic.com/learn/claude-for-work) |
| "Claude Skills training" | [Claude Skills docs](https://code.claude.com/docs/en/skills) + this repo's [examples/](../../examples/) |
| "Claude MCP training" | [MCP documentation](https://modelcontextprotocol.io) — connect Gmail, Notion, HubSpot and more |
| "Build-to-Sell Bootcamp" | [CONTRIBUTING.md](../../CONTRIBUTING.md) — learn agent design by building one; the [Agent Design Guidelines](../../CONTRIBUTING.md#-agent-design-guidelines) are the curriculum |

---

## ❓ FAQ

**Is this really free?** Yes. MIT licensed, like the rest of The Agency. No email gate, no upsell.

**How is this different from the paid "70 AI specialists" products?** Same promise — an AI specialist for every business function, pre-configured, set up in minutes. Differences: these prompts are open (you can read and edit every instruction), community-maintained (they improve over time), versioned in git, and installable as real Claude Code subagents rather than copy-paste prompts. What paid products bundle is mostly packaging and video training; the links above cover that ground for free.

**Do I need all 70?** No. Install the pack, then use the 5–10 that match your week. They're subagents — the unused ones cost nothing.

**Will the output "sound like me"?** Out of the box it sounds like an expert. Give any specialist your context once per session (or via a Project/CLAUDE.md) and it sounds like your expert. See setup above.

**Can I customize a specialist?** That's the point. Each one is a Markdown file — edit it, and if your version is better, [contribute it back](../../CONTRIBUTING.md).

**What about the other ~150 agents in this repo?** This pack is the business-generalist starter set. The full roster adds deep engineering, security, GIS, game-dev, and other technical divisions — run `./scripts/install.sh --list agents` to browse everything.
