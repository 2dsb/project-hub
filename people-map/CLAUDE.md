# people-map — Relationship & Networking

## Contacts

4-field simplified schema:

| Field | Type | Purpose |
|-------|------|---------|
| `name` | string | Full name |
| `contact` | string | Phone, WeChat, or other |
| `maintenance_tier` | enum: `core` / `general` / `weak` | Relationship closeness |
| `contact_dates` | list of `YYYY-MM-DD` | Every interaction that deepened the connection |

Files stored in `entities/<family-name>-<given-name>.md`.

**Future**: Relationship maintenance reminders — alert when a contact hasn't been reached in too long, based on `maintenance_tier` thresholds and `contact_dates` recency.

## Templates

Networking methods and message templates stored as reference files at the people-map root. These are practical playbooks, not idea entities — duplicates from idea-lab are intentional.
