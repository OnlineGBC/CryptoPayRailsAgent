# StablePayGuard — Business Scenario

------------------------------------------------------------------------

## Ideal Customer Profile

The highest-value customer for this platform is a **large global enterprise**
paying vendors, contractors, or partners across multiple countries at high
volume.

| Signal | Why It Matters |
|---|---|
| Cross-border payment volume | SWIFT wires cost $35–$75 each and take 1–5 days. USDC on Base costs $0.02 and settles in 2 seconds. At 500 international payments/month the fee savings alone are $17,500–$37,500/month. |
| High invoice volume | Human review of every invoice costs $15–$50 in staff time. At 1,000 invoices/month that is $15,000–$50,000/month in AP labor that automation eliminates for routine transactions. |
| Audit and compliance requirements | Blockchain audit trail is immutable and independently verifiable without internal system access — critical for SOX compliance, external audit, and fraud investigation. |
| Crypto treasury or digital asset strategy | Increasingly common among Fortune 500 companies. Paying vendors in USDC avoids FX conversion entirely when the treasury already holds stablecoins. |
| Globally distributed workforce | Contractor in Singapore, vendor in Germany, supplier in Brazil — one payment rail, same cost, same speed, regardless of destination. |

### Industries With the Strongest Fit

| Industry | Specific Pain Point Solved |
|---|---|
| Technology (large enterprise) | Global SaaS vendor payments, remote contractor disbursements |
| Manufacturing | Cross-border supplier payments, multi-currency invoice settlement |
| Healthcare | International lab vendor payments, contractor reimbursements across jurisdictions |
| Real Estate | Cross-border property management, international contractor payments |
| Retail / E-commerce | Global fulfillment partner settlements, international marketplace fees |
| Professional Services | Cross-border subcontractor payments, international expert fees |
| Non-Profit / NGO | Grant disbursements to international programs with full audit trail |
| Government / Public Sector | Vendor payments within procurement rules, independently auditable |

The common thread: **any large organization making repetitive cross-border
payments within known rules, where the cost of human approval and wire
transfer friction is significant.**

------------------------------------------------------------------------

## The Core Problem This Solves

Traditional Accounts Payable works like this:

1. Invoice arrives
2. Human reviews it
3. Human checks budget
4. Human checks vendor approval
5. Human approves payment
6. Payment executes
7. Human files the record

This process costs time, money, and introduces human error — for every
single invoice, including the routine $1,800 AWS bill that has arrived on
the same date every month for three years.

StablePayGuard changes the model:

> **Humans define the rules once. AI agents execute within those rules
> continuously. The smart contract enforces the rules autonomously.
> Humans only act on exceptions.**

------------------------------------------------------------------------

## Why This Needs Crypto — And When It Doesn't

This is an honest answer. The enforcement logic — budget limits, per-tx
caps, vendor approval, time windows — can technically be built without
crypto. Tools like Coupa, Tipalti, and Bill.com do something similar
with traditional databases.

**What you lose without crypto:**

| Capability | Traditional Database | Blockchain Smart Contract |
|---|---|---|
| Audit trail integrity | Internal database — can be edited by a DBA, wiped in a breach, or altered by an insider | Immutable — no one, including the company itself, can alter a confirmed transaction |
| Enforcement authority | Runs on servers the company controls — a compromised server or rogue admin can bypass rules | Smart contract cannot be bypassed even by the people who wrote it |
| Cross-border settlement | SWIFT wire: $35–$75, 1–5 days, multiple intermediaries | USDC on Base: $0.02, 2 seconds, no intermediaries |
| Independent verifiability | Requires internal system access for audit | Anyone with the contract address can verify every transaction |
| Fraud surface | Any human in the approval chain, any server in the payment path | Only the policy owner wallet can change rules |

**When crypto is not necessary:**
A purely domestic company paying five local vendors in USD, with no
cross-border volume, no external audit requirement, and simple AP needs
does not need this platform. A spreadsheet and a bank transfer work fine.

**When crypto is clearly the right choice:**
- Cross-border payment volume where wire fees are a real cost
- Industries with external audit or compliance requirements where
  audit trail integrity must be beyond internal question
- Companies already holding crypto or stablecoin treasuries
- Organizations paying global contractors where banking access varies

------------------------------------------------------------------------

## Cross-Border Payment Economics

### $1,000 payment to a contractor in Singapore

| Method | Sender Fee | Receiver Fee | FX Cost | Settlement Time |
|---|---|---|---|---|
| SWIFT wire | $25–$50 | $10–$25 | 1–3% spread | 1–5 business days |
| PayPal International | 3–5% ($30–$50) | None | 2–4% spread | Minutes to days |
| **USDC on Base** | **~$0.02** | **None** | **None (stablecoin)** | **~2 seconds** |

At 500 international payments per month, SWIFT costs $17,500–$37,500 in
fees alone. USDC on Base costs approximately $10.

### Why Base is the right network for enterprise use

| Property | Detail |
|---|---|
| Cost per transfer | ~$0.01–$0.05 regardless of amount sent |
| Settlement time | ~2 seconds (practical finality) |
| Full finality | ~1 minute (statistically irreversible) |
| USDC type | Native — issued directly by Circle, not bridged |
| Security model | Ethereum L2 — inherits Ethereum's security |
| Institutional backing | Operated by Coinbase — compliance-friendly |
| Regulatory clarity | USDC issued under US money transmission licenses |

------------------------------------------------------------------------

## How It Works — Agent A: SaaS Vendor Payments

### The Scenario

A global enterprise pays three SaaS vendors every month: AWS, GitHub,
and Datadog. The rules are fixed:

- Total monthly budget: $15,000
- Maximum per transaction: $2,000
- Approved vendors only
- Payments only within the current calendar month

### PHASE 1 — One-Time Human Setup

| Step | Who | What They Do | Time |
|---|---|---|---|
| 1 | CFO / AP Manager | Decides which vendors are approved: AWS, GitHub, Datadog | 10 min |
| 2 | CFO / AP Manager | Records each vendor's USDC payment wallet address | 10 min |
| 3 | CFO / AP Manager | Generates a cryptographic hash of the approved vendor list — a tamper-proof fingerprint stored on-chain | 2 min |
| 4 | CFO / AP Manager | Opens the Policies tab, creates the policy: agent wallet, token, $15,000 budget, $2,000 per-tx limit, valid date window, purpose hash | 2 min |
| 5 | CFO / AP Manager | Clicks Deploy — policy is written to the blockchain permanently | 1 min |
| 6 | IT / Dev | Configures Agent A to monitor the AP invoice inbox via email API, webhook, or vendor feed | 1 hour |
| 7 | Vendors | Already send structured invoices — no change needed for most SaaS vendors | 0 min |

**Total human setup time: approximately 1.5 hours, done once.**

---

### PHASE 2 — Ongoing Agent Operation (No Human Required)

When an invoice arrives from AWS for $1,800:

| Step | Who | What Happens |
|---|---|---|
| 1 | Agent A | Detects new invoice in the AP inbox |
| 2 | Agent A | Parses vendor name, amount, due date, payment wallet address |
| 3 | Agent A | Checks: is this vendor on the approved list? Does the wallet address match the registered AWS address? |
| 4 | Agent A | Calls the PolicyManager smart contract: "Can I pay $1,800 against policy POL-101?" |
| 5 | Smart Contract | Checks: amount ≤ per-tx limit ($1,800 ≤ $2,000) ✅ |
| 6 | Smart Contract | Checks: running total + amount ≤ monthly budget ($12,400 + $1,800 ≤ $15,000) ✅ |
| 7 | Smart Contract | Checks: today is within the valid date window ✅ |
| 8 | Smart Contract | Checks: vendor hash matches approved vendor list ✅ |
| 9 | Smart Contract | Approves the payment, updates running spend total on-chain |
| 10 | Agent A | Executes USDC transfer to AWS wallet — settles in ~2 seconds |
| 11 | Smart Contract | Emits PaymentApproved event — permanently recorded on-chain |
| 12 | Dashboard | Transaction appears in real time: amount, vendor, policy ID, network hash |
| 13 | CFO | Sees it on the dashboard — no action needed |

**Total human time for this payment: zero minutes.**

---

### PHASE 3 — Exception Handling (Human Back in the Loop)

| Situation | What the Contract Does | What the Agent Does | Human Action Required |
|---|---|---|---|
| Invoice for $1,800 from AWS (normal) | Approves | Pays | None |
| Invoice for $2,400 from AWS (over per-tx limit) | Rejects | Flags for human review | CFO decides: approve as exception or reject |
| Invoice from unknown vendor "QuickInvoice LLC" | Rejects — not on approved list | Flags for human review | AP Manager investigates |
| Monthly budget reaches $14,800 — $600 invoice arrives | Rejects — would exceed $15,000 | Flags for human review | CFO decides: increase budget or defer to next month |
| Invoice arrives after policy expiry date | Rejects — policy expired | Flags for human review | CFO renews policy for new month |
| Vendor changes their payment wallet address | Rejects — hash mismatch | Flags for human review | AP Manager verifies and updates approved vendor list |
| Duplicate invoice submitted twice | Rejects — budget already debited | Flags as duplicate | AP Manager confirms and closes |
| Invoice amount is $0 (data error) | Rejects — amount invalid | Flags as malformed | AP Manager contacts vendor |

------------------------------------------------------------------------

## What the CFO Sees on the Dashboard

| Dashboard Element | What It Shows | Why It Matters |
|---|---|---|
| Policies KPI | Number of active policies | How many agent mandates are running |
| Payments Executed KPI | Running count of approved transactions | Volume of autonomous activity |
| Monthly Volume KPI | Total USD processed this period | Budget consumption at a glance |
| Approval Rate KPI | % of transactions approved vs. rejected | High rejection rate signals a policy needs updating |
| Transactions tab | Every payment: vendor, amount, policy ID, status, network hash | Full ledger — click any hash to verify on-chain |
| Activity feed | Chronological log of all events with timestamps | Real-time awareness without reviewing every transaction |
| Analytics tab | Weekly volume chart, status breakdown, live Uniswap token prices | Trend visibility and live crypto FX rates |
| Remaining budget | Total budget minus spent amount | Never surprised by budget exhaustion |

------------------------------------------------------------------------

## Traditional AP vs. StablePayGuard

| Capability | Traditional AP | StablePayGuard |
|---|---|---|
| Payment approval | Human reviews every invoice | Smart contract enforces rules automatically |
| Audit trail | Internal database — can be edited | Immutable blockchain record — cannot be altered |
| Budget enforcement | Policy document + manual check | Hard-coded in smart contract — mathematically enforced |
| Vendor verification | Spreadsheet or ERP lookup | Cryptographic hash comparison on-chain |
| Exception handling | Everything is an exception | Only true exceptions reach a human |
| Cross-border speed | 1–5 business days | ~2 seconds |
| Cross-border cost | $35–$75 per wire | ~$0.02 per transaction |
| Processing cost | $15–$50 per invoice in staff time | Near zero for routine payments |
| Auditability | Requires internal system access | Anyone with the contract address can verify |
| Fraud surface | Any human in the approval chain | Only the policy owner wallet can change rules |

------------------------------------------------------------------------

## An Honest Note on Security

The statement "nobody can authorize a payment that violates the policy"
is the ideal — not an unconditional guarantee. It holds true **as long
as the smart contract code has no bugs and the owner's private key is
not compromised.**

Known risks and how to address them in production:

| Risk | What Could Happen | Mitigation |
|---|---|---|
| Bug in smart contract | A logic error could allow payments that should be rejected | Professional audit by firms like OpenZeppelin or Certik before production |
| Private key compromise | Attacker becomes owner and can change policies | Hardware wallet (Ledger/Trezor) or multi-signature requiring 2-of-3 approvals |
| Compromised agent wallet | Attacker calls approvePayment within policy limits | Policy limits contain the blast radius — attacker cannot exceed what the policy allows |
| Reentrancy attack | Malicious contract loops back during payment execution | Use OpenZeppelin's ReentrancyGuard in production contract |

The current `PolicyManager.sol` is a prototype. A production deployment
would require a professional security audit before real funds are managed.
This is standard practice — not a weakness unique to this platform.

The key point remains: even with these caveats, a well-audited smart
contract with multisig ownership is dramatically more secure than a
human approval chain, where a single employee with system access can
alter records, approve fraudulent invoices, or cover their tracks.

------------------------------------------------------------------------

## The Fundamental Principle

The smart contract is not a convenience — it is the enforcement layer.

The agent does not need to be trusted. The CFO does not need to monitor
every payment. The AP team does not need to touch routine invoices.

The rules are on-chain. The contract enforces them. A rogue employee
cannot override them. A compromised server cannot bypass them. Even the
company that deployed the contract cannot silently alter a payment
record after the fact.

**That is what makes this fundamentally different from every existing
AP automation tool — and why the blockchain layer is not optional.**

------------------------------------------------------------------------

------------------------------------------------------------------------

## How It Works — Agent B: Global Contractor Payments

### The Scenario

A global enterprise pays independent contractors across multiple countries
every two weeks. Contractors are pre-approved by procurement and legal.
Payments are made in USDC to avoid FX conversion costs and delays.
The rules are:

- Total monthly budget: $50,000
- Maximum per transaction: $5,000 (per contractor per pay run)
- Pre-approved contractors only — verified wallet addresses
- Payments only during business hours (Monday–Friday, 9am–6pm UTC)
  to ensure a human team is available if anything goes wrong
- Each payment must reference the active contractor agreement hash

---

### PHASE 1 — One-Time Human Setup

| Step | Who | What They Do | Time |
|---|---|---|---|
| 1 | Legal / Procurement | Approves contractor roster — reviews contracts, verifies identities, confirms right-to-work in each jurisdiction | 1–2 days (done as part of normal onboarding) |
| 2 | Procurement / AP Manager | Records each contractor's USDC wallet address — verified directly with contractor to prevent substitution fraud | 30 min per contractor |
| 3 | Legal | Finalises the master contractor agreement document — standard terms covering payment, IP, confidentiality | Existing process |
| 4 | AP Manager | Generates a cryptographic hash of the approved contractor list and master agreement — both stored in the policy as purposeHash | 5 min |
| 5 | AP Manager | Opens the Policies tab and creates Agent B's policy: $50,000 monthly budget, $5,000 per-tx limit, valid date window (current month), USDC token, purpose hash | 5 min |
| 6 | AP Manager | Sets business hours enforcement: validFrom = Monday 9am UTC, validUntil = Friday 6pm UTC, renewed each week | 2 min per week |
| 7 | AP Manager | Clicks Deploy — policy written to blockchain | 1 min |
| 8 | IT / Dev | Configures Agent B to monitor the contractor invoice inbox and connect to the payroll schedule | 1–2 hours |
| 9 | Contractors | Notified of USDC payment setup — provide wallet address, receive test transaction to confirm | 15 min per contractor |

**Total human setup time: 1–2 days for initial contractor onboarding (mostly existing procurement process), 2 hours for technical setup, done once.**

---

### PHASE 2 — Ongoing Agent Operation (No Human Required)

When a contractor in Singapore submits an invoice for $3,200:

| Step | Who | What Happens |
|---|---|---|
| 1 | Agent B | Detects new invoice — contractor name, amount, wallet address, invoice reference |
| 2 | Agent B | Verifies: is this contractor on the approved roster? Does the submitted wallet address match the registered address for this contractor? |
| 3 | Agent B | Verifies: does the invoice reference the current active contractor agreement? (Hash comparison) |
| 4 | Agent B | Checks current time: is it Monday–Friday, 9am–6pm UTC? |
| 5 | Agent B | Calls PolicyManager smart contract: "Can I pay $3,200 against policy POL-102?" |
| 6 | Smart Contract | Checks: $3,200 ≤ $5,000 per-tx limit ✅ |
| 7 | Smart Contract | Checks: running monthly total + $3,200 ≤ $50,000 ✅ |
| 8 | Smart Contract | Checks: current timestamp within valid window ✅ |
| 9 | Smart Contract | Checks: purposeHash matches active contractor agreement ✅ |
| 10 | Smart Contract | Approves payment, updates running spend on-chain |
| 11 | Agent B | Executes USDC transfer directly to contractor's wallet — no bank, no SWIFT, no correspondent fees |
| 12 | Contractor | Receives $3,200 USDC in Singapore in ~2 seconds. No currency conversion needed. No bank hold. |
| 13 | Smart Contract | Emits PaymentApproved event — permanently recorded |
| 14 | Dashboard | Transaction visible in real time with network hash |
| 15 | CFO | Sees it on the dashboard — no action needed |

**Traditional alternative:** SWIFT wire to Singapore bank, $35–$50 sender fee, $15–$25 receiver fee, 2–4 business days, possible intermediate bank deductions.

**With Agent B:** $0.02, 2 seconds, full amount delivered, independently verifiable.

---

### PHASE 3 — Exception Handling (Human Back in the Loop)

| Situation | What the Contract Does | What the Agent Does | Human Action Required |
|---|---|---|---|
| Invoice from approved contractor, correct amount | Approves | Pays | None |
| Invoice from contractor not on approved roster | Rejects — wallet not recognised | Flags for human review | Procurement verifies and onboards contractor, or rejects invoice |
| Contractor submits invoice with updated wallet address | Rejects — wallet mismatch | Flags for human review | AP Manager verifies new address directly with contractor (prevents substitution fraud) |
| Invoice submitted at 11pm UTC (outside business hours) | Rejects — outside valid window | Flags for human review | Agent queues for next business day, or AP Manager manually approves if urgent |
| Monthly budget reaches $48,000 — $3,500 invoice arrives | Rejects — would exceed $50,000 | Flags for human review | CFO decides: increase budget or defer to next month |
| Same invoice submitted twice (duplicate) | Rejects — budget already debited | Flags as duplicate | AP Manager confirms and closes |
| Contractor references outdated agreement version | Rejects — hash mismatch | Flags for human review | Legal confirms whether old agreement is still valid |
| Invoice amount is $6,000 (above per-tx limit) | Rejects — exceeds per-tx cap | Flags for human review | AP Manager splits into two payments or escalates for CFO exception approval |
| Contractor in sanctioned jurisdiction | Rejects — wallet not on approved list | Flags for human review | Legal / Compliance reviews — never reaches the contract |

---

### What Makes Contractor Payments Specifically Better With This System

Traditional contractor payments across borders involve:
- Bank wire fees on both ends ($50–$75 total)
- 2–5 day delays while correspondent banks process
- Currency conversion losses if paying in USD to a non-USD country
- Manual reconciliation of who was paid, when, and how much
- Compliance exposure if a contractor's jurisdiction changes

With Agent B:
- Every contractor payment is on-chain and independently auditable
- No wire fees — $0.02 per transaction regardless of destination
- USDC is a dollar-pegged stablecoin — no FX conversion needed
- The approved wallet list prevents payment redirection fraud
- Business hours enforcement means a human team is always available if an exception occurs
- The smart contract's running total prevents month-end budget overruns

------------------------------------------------------------------------

## How It Works — Agent C: Employee Travel & Expense Reimbursements

### The Scenario

Employees submit travel and expense (T&E) claims after business trips
or client entertainment. Under the current process, claims go to a
manager for approval, then to AP for payment — typically taking 1–2 weeks
and requiring manual policy checks.

The rules under the new system:

- Maximum per claim: $500 (claims above this go to manager approval)
- Claims must match approved expense categories in the company T&E policy
- Each claim must reference the active T&E policy document hash
- Claims processed within 24 hours of submission
- Payments made to the employee's registered USDC wallet or bank

---

### PHASE 1 — One-Time Human Setup

| Step | Who | What They Do | Time |
|---|---|---|---|
| 1 | Finance / HR | Finalises the company T&E policy document — defines approved categories (travel, accommodation, meals, client entertainment), per-category limits, and documentation requirements | Existing process |
| 2 | Finance | Generates a cryptographic hash of the T&E policy PDF — this becomes the purposeHash for Agent C's policy | 2 min |
| 3 | HR / IT | Collects each employee's registered payment wallet or bank account — verified against employee records | Part of onboarding |
| 4 | AP Manager | Creates Agent C's policy on the dashboard: $500 per-tx limit, USDC token, purpose hash of T&E policy, valid for current quarter | 5 min |
| 5 | AP Manager | Deploys policy to blockchain | 1 min |
| 6 | IT / Dev | Integrates Agent C with the expense submission system (e.g. Concur, Expensify, or internal portal) via API | 2–4 hours |
| 7 | Employees | Notified of new instant reimbursement process — claims under $500 paid within 24 hours | 0 min (benefit to employee) |

**Total human setup time: 2–4 hours for technical integration, done once.
The T&E policy itself is an existing document — no additional work required.**

---

### PHASE 2 — Ongoing Agent Operation (No Human Required)

When an employee submits a $240 claim for client dinner receipts:

| Step | Who | What Happens |
|---|---|---|
| 1 | Employee | Submits expense claim via the company portal: category (client entertainment), amount ($240), receipts attached, date |
| 2 | Agent C | Receives the claim via API from the expense portal |
| 3 | Agent C | Checks: does this expense category appear in the approved T&E policy? (client entertainment — yes) |
| 4 | Agent C | Checks: is the amount within the per-category limit defined in the T&E policy? ($240 within client entertainment limit — yes) |
| 5 | Agent C | Checks: is the claim referencing the current active T&E policy hash? |
| 6 | Agent C | Calls PolicyManager smart contract: "Can I pay $240 against policy POL-103?" |
| 7 | Smart Contract | Checks: $240 ≤ $500 per-tx limit ✅ |
| 8 | Smart Contract | Checks: running total within monthly budget ✅ |
| 9 | Smart Contract | Checks: within valid policy window ✅ |
| 10 | Smart Contract | Checks: purposeHash matches current T&E policy ✅ |
| 11 | Smart Contract | Approves payment, updates running spend on-chain |
| 12 | Agent C | Executes USDC transfer to employee's registered wallet |
| 13 | Smart Contract | Emits PaymentApproved event with claim reference |
| 14 | Dashboard | Reimbursement logged in real time — Finance can see all claims |
| 15 | Employee | Receives $240 USDC within seconds of submission — not 2 weeks |

**Traditional alternative:** Claim submitted → manager approves (2–3 days) → AP processes (3–5 days) → bank transfer (1–2 days) → employee reimbursed after 1–2 weeks.**

**With Agent C:** Submission to reimbursement in under 60 seconds for any claim under $500 that matches policy.

---

### PHASE 3 — Exception Handling (Human Back in the Loop)

| Situation | What the Contract Does | What the Agent Does | Human Action Required |
|---|---|---|---|
| $240 client dinner claim, valid receipts | Approves | Pays | None |
| $650 claim (above $500 per-tx limit) | Rejects — exceeds per-tx cap | Routes to manager approval queue | Manager reviews and approves or rejects manually |
| Claim category not in T&E policy (e.g. gym membership) | Rejects — category not covered | Flags for human review | Finance confirms whether to allow as exception |
| Employee submits claim referencing outdated T&E policy | Rejects — hash mismatch | Flags for human review | Finance confirms whether old policy still applies (e.g. during policy update transition) |
| Duplicate claim submitted twice | Rejects — already processed | Flags as duplicate | AP Manager confirms and closes |
| Claim submitted by employee who has left the company | Rejects — wallet not on active employee list | Flags for human review | HR confirms status — final expense may be valid |
| Receipt date is 6 months ago (outside claim window) | Rejects — outside valid date window | Flags for human review | Finance decides whether to allow late claim |
| Employee's registered wallet changed | Rejects — wallet mismatch | Flags for human review | HR verifies new wallet directly with employee (prevents fraudulent redirection) |

---

### What Makes T&E Reimbursement Specifically Better With This System

Traditional expense reimbursement is one of the most complained-about
processes in any large company:
- Employees wait 1–2 weeks to be reimbursed for money they spent out of pocket
- AP teams spend significant time manually checking receipts against policy
- Policy violations are caught after the fact, if at all
- No independent audit trail — disputes rely on email chains and spreadsheets

With Agent C:
- Claims under $500 that match policy are paid within seconds
- The T&E policy hash means Agent C is always enforcing the current approved version
- If Finance updates the T&E policy, they generate a new hash, update the policy, and Agent C instantly enforces the new rules for all future claims
- Employees see reimbursement as a differentiator — instant payment vs. the industry standard of weeks
- Finance gets a real-time dashboard of all T&E spend with full on-chain audit trail

------------------------------------------------------------------------

## All Three Agents Together — The CFO's View

At any point, the CFO sees on the dashboard:

| Agent | Role | Monthly Budget | Spent | Remaining | Transactions |
|---|---|---|---|---|---|
| Agent A | SaaS vendor payments | $15,000 | $12,400 | $2,600 | 8 completed |
| Agent B | Contractor payments | $50,000 | $31,200 | $18,800 | 14 completed, 1 pending |
| Agent C | T&E reimbursements | $25,000 | $8,750 | $16,250 | 37 completed, 2 flagged |

Every row in the Transactions tab links to an on-chain record. Every
exception is in the Activity feed. Every policy rule is permanently
visible on the blockchain.

No AP clerk had to touch any of the 59 completed transactions.
A human was only needed for the 3 flagged exceptions.

**That is the operating model this platform enables.**

------------------------------------------------------------------------

## Production Roadmap

| Phase | What Gets Added | Business Benefit |
|---|---|---|
| Phase 1 — Current | Policy engine, on-chain enforcement, dashboard, Uniswap pricing | Working prototype demonstrating the full concept |
| Phase 2 — Data Layer | PostgreSQL persistence, user authentication, multi-user dashboards, role-based access | CFO, AP Manager, and auditor each see their relevant view |
| Phase 3 — Real Payment Rails | Mainnet deployment, real USDC settlement, bank API integration (ACH/SWIFT) for hybrid fiat/crypto flows | Actual money movement at production scale |
| Phase 4 — AI Agent Platform | Anomaly detection, spending predictions, policy auto-optimization, multi-agent coordination | Proactive controls — system flags unusual patterns before they become problems |
