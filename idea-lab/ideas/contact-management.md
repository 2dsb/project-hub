---
id: idea-20260601-8a3b1c
title: Contact Management System
tags:
- contacts
- crm
- relationships
- personal-data
summary: "A systematic contact management system is needed to record people’s details, proactively maintain relationships by “catering to their interests”—remembering what they care about—and unlock latent network value. The two-way information asymmetry makes resources invisible, so the system tracks interest points and triggers contact when relevant content, events, or follow-ups arise. Monetizing the network involves demand matching, information arbitrage, and skill resource pooling. This could become a personal skill with a contact entity data layer and AI-driven reminders for interest-based outreach."
importance: 0
connections:
  - type: project
    slug: ai-ability
  - type: idea
    slug: "contact-management-simplified-schema"
---
# Contact Management System

Record people I know, with the following fields:
- Name
- Phone number
- Relationship to me
- Identity / occupation
- Birthday

Resource visibility (the two-way information asymmetry problem):
- My problem: the resources I can mobilize (direct + indirect) are invisible to others → others won't proactively come to me
- Others' problem: it's hard for me to gauge how many "hidden resources" someone really has (their network, skills, information channels)
- Leveraging second-degree resources: how to reach the larger resource network behind direct contacts?
  - Example: A can't help me directly, but A's friend B happens to have exactly what I need
  - Key: getting A to open up their network for me requires A's sufficient trust in me + clear understanding of my needs

Relationship maintenance features:
- Core principle: cater to their interests — staying in touch isn't about generic greetings, it's about "remembering what they care about"
- Record their interest points, focus areas, and recent updates; reach out naturally at these moments:
  - Birthday greetings (basic)
  - Spotting content they'd be interested in (articles, podcasts, events, opportunities) → forward + a note saying "thought you might be interested"
  - New developments in their field (industry news, policy changes) → share + ask what they think
  - Follow-up on concerns/goals they recently mentioned → "How's that XX thing you mentioned last time?"
  - Shared memory triggers (old photos, anniversaries, alma mater news)
- Periodic contact reminders (e.g., "It's been N months since you last contacted X — want to reach out?") — but the reminder is just a trigger; the actual contact content must be based on "cater to their interests" records
- Maintenance effort tiering: core relationships (proactively dig up topics) vs. regular relationships (birthdays + occasional content sharing) vs. weak ties (stay visible without over-investing)

Monetizing your network (creating value through connections):
- Demand matching: ask contacts about their respective needs/resources, match supply and demand, facilitate deals or collaborations, creating a triple win (both sides benefit + I gain referral fees/favors/strengthened relationships)
- Information arbitrage: knowing what A understands and what B needs, bridging information asymmetry
- Skill resource pool: knowing who knows what and who lacks what — be the resource dispatcher
- Collaboration matchmaking: identifying people with shared interests or complementary skills and facilitating project partnerships
- Opportunity distribution: quickly matching opportunities (jobs/projects/resources) to the right people when you spot them

Purpose: as the number of people I know grows, I need systematic contact information management, proactive maintenance of important relationships, and — building on relationship maintenance — uncovering the latent value of my network.

## Possible Skill Direction

This idea may be suitable as a "contact relationship maintenance" personal skill, covering CRUD for contact data, maintenance reminders, and matching assistance for network value creation. Core features may include:

- **Data layer**: Contact entities (under `entities/`), containing basic info + interest points / focus areas + recent updates
- **Maintenance side**: Smart reminders based on the "cater to their interests" principle — not just nudging you on a schedule to send a message, but proactively prompting "Want to forward this to X?" when the AI browses content matching a contact's interests
- **Value-creation side**: Demand/resource matching queries — when the user mentions a need, the AI searches the contact database for who might have relevant resources or skills
- **Daily integration**: When there are contact-related events that day (birthdays, pending replies, promise follow-ups), write them into the daily reminders section

This skill is more complex than the other three (illness-reframing / knowledge-reconnection / low-energy-cognitive), as it involves entity schema design, data storage structures, and multi-dimensional queries. Before implementation, the field specification and storage location for contact entities need to be determined first.
