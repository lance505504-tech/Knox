# Cape31 Website News Update — Instructions for Claude

You have been given this file alongside a Cape31 regional website HTML file.
Your job is to research and update the news section of that website.
Follow these steps exactly, in order.

---

## Step 1 — Read the HTML file

Read the uploaded HTML file. Find out which region the site covers by looking at the page title or hero heading. It will be one of: UK, International, Mediterranean, South Africa, Australia, Hong Kong, Ireland, or United States.

Confirm to the user: "I can see this is the Cape31 **[region]** website. I'll now search for the latest news."

---

## Step 2 — Search for the latest news

Search the web for recent Cape31 news for that region. Use these sources:

**For all regions:**
- https://www.cape31class.com/news
- https://www.livesaildie.com/tag/cape31/
- https://afloat.ie/sail/sailing-classes/cape-31

**For UK specifically:** also search:
- https://www.cape31class.com/news/categories/uk
- Search: "Cape31 UK 2026 race results"

**For Mediterranean / Europe:** also search:
- https://www.cape31class.com/news/categories/eu
- Search: "Cape31 Med Circuit 2026"

**For South Africa:** also search:
- https://sa.cape31.com/sa-results/
- Search: "Cape Doctor Editions Cape31 2026"

**For Australia:** also search:
- https://www.cape31.com.au/news
- Search: "Cape31 Australia 2026 racing"

**For United States:** also search:
- Search: "Cape31 United States 2026 regatta results"
- Search: "Pacific Yankee Cape31 2026"

Search broadly. Look for race reports, regatta results, class news, and fleet updates from the past 12 months. Find at least 3 news items and ideally up to 6.

---

## Step 3 — Find the news section in the HTML file

Look through the HTML for the section that contains news articles. It will be marked with `id="news"` or contain a heading like "Latest News", "C31 News" or "UK Fleet News". The news items will be inside this section.

---

## Step 4 — Update the news section

Replace the existing news items with the new ones you found. For each news item include:

- **Date** — the date of the article or event (e.g. "March 2026")
- **Category tag** — e.g. "Race Report", "UK", "Med Circuit", "Results"
- **Headline** — the title of the article or event
- **Short summary** — 1–2 sentences describing what happened. Write this yourself in plain English based on what you found. Do not copy text directly from the source.
- **Link** — a "Read More" link to the original article

Keep the same HTML structure and CSS classes as the existing news items — just replace the content inside them. Do not change any other part of the page.

If you cannot find enough real news, keep some of the existing items and add the new ones at the top. Most recent item should always be first.

---

## Step 5 — Output the updated file

Output the complete updated HTML file. Name it with today's date added to the filename — for example if the original was `Cape31-UK-v2.html`, name the output `Cape31-UK-v2-[DDMM].html` where DDMM is today's date (e.g. 0604 for 6 April).

Tell the user:
- How many news items are now in the page
- What the newest item is and its date
- The filename to upload to GitHub

---

## Step 6 — What to do with the file

Tell the user:

> "Your updated file is ready. To publish it:
> 1. Download the file using the button above
> 2. Go to github.com and sign in
> 3. Find the repository for this region
> 4. Click on index.html → click the pencil icon → scroll down → click 'Upload file'
> 5. Upload the new file, rename it index.html, and click 'Commit changes'
> 6. The live website will update within 2 minutes"

---

## Important rules

- Only update the news section. Do not change anything else on the page.
- Do not copy text word-for-word from news articles — summarise in your own words.
- If a news article is behind a paywall and you cannot read it, use the headline and any visible summary only.
- If you cannot find any recent news (less than 12 months old), say so and ask the user if they want to keep the existing news or remove old items.
- Always output the complete HTML file, not just the changed section.
