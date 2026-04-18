# Cold Email Deliverability — The Fundamentals Every Sender Must Know

**Channel:** QuickMail — Jeremy Chatelaine  
**URL:** https://www.youtube.com/@QuickMail  
**Collected:** April 2026  

---

## Transcript Summary

Jeremy covers the complete deliverability stack — from 
domain setup to inbox placement monitoring — with the 
depth of someone who has been building outbound infrastructure 
for over a decade.

**On why deliverability is the foundation:**
"You can have the best copy in the world. 
If your email lands in spam, your reply rate is zero. 
Deliverability is not a technical detail — 
it's the prerequisite for everything else."

**On authentication setup:**
The three authentication records every cold email domain needs:
- SPF: Specifies which servers are authorized to send on behalf 
  of your domain
- DKIM: Adds a digital signature to every email verifying 
  it hasn't been tampered with
- DMARC: Policy that tells inbox providers what to do 
  if SPF or DKIM fail

Jeremy notes that 40%+ of B2B cold email senders are missing 
at least one of these — and paying for it in spam placement.

**On inbox rotation:**
QuickMail pioneered inbox rotation — the practice of 
distributing sends across multiple inboxes to protect 
individual sender reputation. 

The principle: inbox providers monitor sending volume per address. 
Sudden spikes trigger spam filters. Distributing volume across 
3-5 inboxes keeps each under the radar while maintaining 
campaign-level volume.

**On warm-up:**
Jeremy recommends minimum 3 weeks of warm-up before 
first real send. QuickMail's warm-up tool sends and 
receives automated emails between participating inboxes — 
training inbox providers to see the account as legitimate 
before real sends begin.

**On monitoring:**
Key deliverability metrics Jeremy tracks:
- Bounce rate: keep below 3%
- Spam complaint rate: keep below 0.1%
- Open rate by inbox provider (Gmail vs. Outlook behave differently)
- Inbox placement rate (separate from open rate — 
  requires a seed list test)

**On the relationship between deliverability and reply rate:**
A 1% improvement in inbox placement rate translates directly 
to a 1% improvement in potential reply rate. 
For a campaign sending 10,000 emails, 
1% inbox placement improvement means 100 more emails seen.

---

## Key Insights Extracted

1. Authentication (SPF, DKIM, DMARC) is the non-negotiable 
   foundation — 40%+ of senders are missing at least one
2. Inbox rotation distributes sender reputation risk 
   across multiple inboxes — now a standard best practice
3. Minimum 3 weeks warm-up before first send — 
   this is not optional
4. Spam complaint rate above 0.1% triggers inbox provider 
   penalties that are difficult to recover from
5. Inbox placement and open rate are different metrics — 
   use a seed list to measure true inbox placement
