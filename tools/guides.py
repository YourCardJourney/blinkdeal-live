"""Write the four store guide pages - /myntra-gold-coin-offers/ and friends.

These are the pages web search can land on. The home page is a wheel with
almost no words; each guide explains one store's gold offers in plain text,
answers the questions people actually type, and sends them to the live board.

Edit the STORES data below, then run:   python tools/guides.py
It rewrites the four pages and sitemap.xml. Keep facts general and true -
the boards show the live numbers, these pages explain how to read them.
"""
import html
import json
import os
from datetime import date

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = "https://blinkdeal.live"
TODAY = date.today().isoformat()

# Written once, shared by every guide: how to tell a good gold coin deal.
CHECKS = [
    ("Purity", "24K coins are usually 999 or 995 fine gold; 22K coins are 916. A 22K coin holds less gold per gram, so it will always look cheaper per gram - compare the gold inside, not the sticker."),
    ("Weight", "The gold value is weight × purity × today's rate. Coins from 1 g to 10 g are the sweet spot: below 1 g the making charge swamps the metal."),
    ("The price you actually pay", "Take the listed price, then the coupon or offer that really applies to that product. Store prices in India already include 3% GST on gold."),
    ("The rate you compare against", "Jewellers' daily rates differ. A refinery's rate makes almost every coin look cheap; a big jeweller's retail rate is the stricter test. Pick one and stick to it."),
]

STORES = [
    {
        "id": "myntra", "name": "Myntra", "slug": "myntra-gold-coin-offers",
        "board": "https://blinkdeal.yourcardjourney.store", "board_name": "BlinkDeal for Myntra",
        "title": "Myntra Gold Coin Offers – BlinkDeal Coupons",
        "h1": "Myntra gold coin offers, <em>ranked in a blink.</em>",
        "desc": "How Myntra's BlinkDeal flash coupons on gold coins work, which coins beat today's gold rate, and a live board that ranks every Myntra gold coin the moment the coupon goes live.",
        "lede": "Myntra runs short flash coupons on its gold coins – BlinkDeals. They last minutes, and the best coins sell out first. The BlinkDeal board has every Myntra gold coin already priced against today's gold rate, so when the coupon fires you know which coins cost less than the gold in them.",
        "how": [
            ("The BlinkDeal coupon", "Codes like <b>BLINKDEAL6</b> or <b>BLINKDEAL8</b> take a fixed percentage off Myntra's listed price. A deal usually runs for around ten minutes."),
            ("One coupon per order", "Myntra allows a single coupon on an order, and during a BlinkDeal that coupon is the deal – nothing else stacks on top."),
            ("The brands", "Kalyan Jewellers, Malabar Gold &amp; Diamonds, Joyalukkas, Mia by Tanishq, Bhima, P N Gadgil, C Krishniah Chetty, Muthoot Pappachan, PMJ Jewels, Bangalore Refinery and more – 1 g to 10 g, 22K and 24K."),
            ("Stock runs out", "Myntra shows how many of each coin are left. Popular 5 g and 10 g coins can sell out within minutes of a deal starting."),
        ],
        "faq": [
            ("What is a Myntra BlinkDeal?", "A short flash coupon Myntra runs on its gold coin listings, usually for about ten minutes, with codes such as BLINKDEAL6 or BLINKDEAL8 that take a fixed percentage off the listed price."),
            ("Can I use another coupon with a BlinkDeal on Myntra?", "No. Myntra allows one coupon per order, and during a BlinkDeal the BlinkDeal code is that coupon."),
            ("How do I know if a Myntra gold coin is a good deal?", "Compare the price after the BlinkDeal coupon with the value of the gold in the coin – its weight times its purity at today's gold rate. The BlinkDeal board does this for every coin and shows the gap."),
            ("When is the next Myntra BlinkDeal?", "Myntra does not announce them in advance. The BlinkDeal board opens when a deal starts and rests when it ends, so keep blinkdeal.live handy."),
        ],
    },
    {
        "id": "amazon", "name": "Amazon", "slug": "amazon-gold-coin-offers",
        "board": "https://amazongold.yourcardjourney.store", "board_name": "AmazonGold",
        "title": "Amazon Gold Coin Offers – Coupons & Credit Card Offers",
        "h1": "Amazon gold coin offers, <em>priced against gold.</em>",
        "desc": "Gold coins, bars and jewellery on Amazon.in priced against today's gold rate – with Amazon's coupon and your credit card offer stacked in, so you can see what really beats the gold rate.",
        "lede": "Amazon.in sells gold coins, bars and gold jewellery from dozens of jewellers and refiners, and the discount comes from more than one place – a store coupon, a bank card offer, sometimes both. The AmazonGold board stacks them the way checkout would, then compares the result with the gold in each piece.",
        "how": [
            ("Coupons", "Amazon's gold coupons often apply to jewellery – chains, pendants, earrings – and not to coins and bars. The board only applies a coupon where it actually works."),
            ("Credit card offers", "Bank credit card offers are applied on the price after the coupon, which is how Amazon's checkout calculates them."),
            ("Coins, bars and jewellery", "24K coins and bars from refiners and jewellers, plus 22K and 18K jewellery from the big jewellery brands."),
            ("Prices move", "Amazon reprices gold listings often. The board re-reads them through the day and shows how old each price is."),
        ],
        "faq": [
            ("Do Amazon coupons work on gold coins?", "Often not. Amazon's gold coupons usually cover jewellery, not coins and bars. Check the coupon's terms on the product page; the AmazonGold board marks where a coupon does not apply."),
            ("Can I combine an Amazon coupon with a credit card offer on gold?", "Where both apply, yes – the card offer is calculated on the price after the coupon. The AmazonGold board stacks them in that order."),
            ("Is buying a gold coin on Amazon cheaper than a jeweller?", "Sometimes, during coupon and bank offer days. Compare the final price with the gold value at a jeweller's rate – that is exactly what the board shows."),
            ("Are EMI offers included?", "No. EMI discounts depend on your card and tenure, so the board leaves them out and shows the price you pay upfront."),
        ],
    },
    {
        "id": "flipkart", "name": "Flipkart", "slug": "flipkart-gold-coin-offers",
        "board": "https://flipkartgold.yourcardjourney.store", "board_name": "FlipkartGold",
        "title": "Flipkart Gold Coin Offers – Credit Card & Bank Offers",
        "h1": "Flipkart gold coin offers, <em>read the fine print.</em>",
        "desc": "Gold coins, bars and jewellery on Flipkart priced against today's gold rate – purity and weight read from each listing's specs, and credit card bank offers checked against their terms.",
        "lede": "Flipkart lists hundreds of gold coins, bars and jewellery pieces, many from the same brands you see in stores. The FlipkartGold board reads each listing's purity and weight from its specifications – not its title – and prices it against today's gold rate.",
        "how": [
            ("Specs, not titles", "Purity and weight come from the product specifications (Gold Purity, Weight), which are more reliable than listing titles."),
            ("Credit card offers and gold", "Some credit card cashback offers on Flipkart exclude gold in their terms. The board checks an offer's terms before counting it."),
            ("Coupons", "Where Flipkart shows an extra discount or coupon on a listing, the board applies it to that piece."),
            ("Silver is filtered out", "Flipkart's coins and bars store is mostly silver; the board keeps only gold."),
        ],
        "faq": [
            ("Do Flipkart credit card offers apply to gold coins?", "Not always. Several credit card cashback offers on Flipkart exclude gold and jewellery in their terms. The FlipkartGold board only counts an offer if its terms allow gold."),
            ("How do I check the purity of a gold coin on Flipkart?", "Look for the Gold Purity field in the product specifications – for example 24K (995) or 24K (999). Titles can be vague; the specs are what the board uses."),
            ("Is a 22K coin cheaper than a 24K coin on Flipkart?", "Per gram of coin, usually yes – but it holds less gold. Compare the value of the gold inside, not the price per gram of the coin."),
            ("Do gold coins go on sale during Flipkart's big sales?", "Bank offers during large sale events sometimes include gold. The board picks up offers that apply as soon as they appear on the listing."),
        ],
    },
    {
        "id": "ajio", "name": "Ajio", "slug": "ajio-gold-coin-offers",
        "board": "https://ajiogold.yourcardjourney.store", "board_name": "AjioGold",
        "title": "Ajio Gold Coin Offers – Coupons & Card Offers",
        "h1": "Ajio gold coin offers, <em>checked against gold.</em>",
        "desc": "Gold coins, bars and jewellery on AJIO priced against today's gold rate, with AJIO's gold coupon applied – see which pieces cost less than the gold in them.",
        "lede": "AJIO sells gold coins, bars and gold jewellery from well-known jewellers, and runs coupons that can bring a coin close to – or below – the value of its gold. The AjioGold board applies the current AJIO gold coupon to every piece and compares the price with today's gold rate.",
        "how": [
            ("The AJIO gold coupon", "When AJIO runs a gold coupon, the board applies it across the coins and jewellery it covers."),
            ("Coins, bars and jewellery", "Gold coins and bars plus chains, pendants and other gold jewellery from the jeweller brands on AJIO."),
            ("Bank and UPI offers", "AJIO's prepaid offers are often UPI or card cashbacks. They change often; the board reads them when it can."),
            ("Opens when there's a deal", "The AjioGold board opens when a gold deal kicks in, so you are not looking at stale prices."),
        ],
        "faq": [
            ("Does AJIO have coupons for gold coins?", "At times, yes. When AJIO runs a gold coupon, the AjioGold board applies it to the pieces it covers and shows the price after the coupon."),
            ("How do I know if an AJIO gold coin is worth buying?", "Compare the price after the coupon with the value of the gold in the coin – weight times purity at today's rate. The AjioGold board shows that gap for every piece."),
            ("Does the AJIO 'Coupon Applicable' tag mean the coupon works?", "Not always. The tag on a listing is not a guarantee that a code will apply at checkout – always confirm at checkout."),
            ("Is AJIO gold jewellery priced against the gold rate too?", "Yes. For jewellery the board compares the price with the gold content from its purity and weight, so the making charge shows up as the gap."),
        ],
    },
]

CARD_GUIDE = {
    "slug": "credit-card-gold-deals",
    "label": "Credit card gold deals",
    "icon": "../favicon.svg",
    "eyebrow": "Credit cards · gold coins on Myntra, Amazon, Flipkart &amp; Ajio",
    "how_h": "How credit card offers work on gold",
    "faq_h": "Credit cards and gold – questions",
    "cta_url": "../",
    "cta_text": "Open the wheel – pick a store",
    "track": "wheel",
    "title": "Credit Card Gold Deals – Offers on Gold Coins in India",
    "h1": "Credit card gold deals, <em>worked out for you.</em>",
    "desc": "Credit card offers on gold coins, bars and jewellery across Myntra, Amazon, Flipkart and Ajio – which bank offers actually apply to gold, what they stack with, and which coins still beat today's gold rate.",
    "lede": "Buying gold on a credit card can earn a bank discount, cashback or reward points – or nothing at all, because many offers quietly exclude gold. BlinkDeal's boards stack the coupon and the card offer the way checkout does, drop offers whose terms exclude gold, and compare what is left with the value of the gold in each coin.",
    "how": [
        ("Instant bank discounts", "Amazon and Flipkart run bank offers – a percentage off, up to a cap, for a particular bank's cards. On gold they apply to the price after the store coupon."),
        ("Offers that exclude gold", "Many card cashback offers list gold coins and jewellery as exclusions in their terms. The boards read the terms and leave those out, so the saving you see is one you can actually get."),
        ("Coupon plus card", "A store coupon and a card offer can often stack. Myntra is the exception during a BlinkDeal: one coupon per order, and the BlinkDeal code is it."),
        ("Reward points", "Some cards earn points on gold, some don't, and some cap it. Points depend on your card, so the boards show the upfront price; check your card's reward terms before you count them."),
    ],
    "checks": [
        ("Read the offer's exclusions", "Look for 'gold', 'jewellery' or 'bullion' in the exclusions before you rely on a bank offer."),
        ("Check the cap", "A 10% offer capped at ₹1,500 is 10% only up to ₹15,000 – on a 10 g coin it is a much smaller percentage."),
        ("Know how the merchant bills", "Reward rules often depend on how a purchase is categorised. A gold coin from a fashion or marketplace store may be treated differently from a jeweller – check your card's terms."),
        ("Compare with the gold, not the MRP", "A big discount off an inflated price can still cost more than the gold is worth. The boards compare the final price with the gold value at a rate you choose."),
    ],
    "faq": [
        ("Can I buy gold coins with a credit card in India?", "Yes. Myntra, Amazon, Flipkart and Ajio all accept credit cards for gold coins, bars and jewellery. Whether you get a discount or rewards depends on the card and the offer's terms."),
        ("Which credit card offers work on gold coins?", "It changes with every sale. Bank offers on Amazon and Flipkart sometimes include gold and often exclude it. The Amazon and Flipkart gold boards only count an offer when its terms allow gold."),
        ("Do I earn reward points when I buy gold on a credit card?", "Depends on your card. Some cards exclude gold and jewellery from rewards, some cap them, some treat marketplace purchases normally. Check your card's reward terms."),
        ("Can I stack a store coupon with a credit card offer on gold?", "Often, yes – the card offer is calculated on the price after the coupon. During a Myntra BlinkDeal only one coupon applies per order."),
        ("Is buying gold on a credit card a good idea?", "Only if the final price – after coupon and card offer – is close to or below the value of the gold, and you pay the card bill in full. BlinkDeal shows the data points; the decision is yours. It is not investment advice."),
    ],
}

HEAD_SVG = open(os.path.join(ROOT, "about", "index.html"), encoding="utf-8").read()
# Reuse the About page's inline gradient defs + top bar so the guides match it exactly.
DEFS = HEAD_SVG[HEAD_SVG.index('<svg width="0" height="0"'):HEAD_SVG.index('<header class="topbar">')]
TOPBAR = HEAD_SVG[HEAD_SVG.index('<header class="topbar">'):HEAD_SVG.index('</header>') + len('</header>')]
FOOTER = HEAD_SVG[HEAD_SVG.index('<footer>'):HEAD_SVG.index('</footer>') + len('</footer>')]


def strip(s):
    """Plain text for meta tags and JSON-LD."""
    import re
    return html.unescape(re.sub(r"<[^>]+>", "", s))


def store_defaults(st):
    """Fill in the wording a store guide uses; the credit card guide sets its own."""
    st.setdefault("label", f"{st['name']} gold coin offers")
    st.setdefault("icon", f"../marks/{st['id']}.svg")
    st.setdefault("eyebrow", f"{st['name']} · gold coins, bars &amp; jewellery")
    st.setdefault("how_h", f"How {st['name']}'s gold offers work")
    st.setdefault("faq_h", f"{st['name']} gold coins – questions")
    st.setdefault("cta_url", st["board"])
    st.setdefault("cta_text", f"Open the {st['board_name']} board")
    st.setdefault("track", st["id"])
    return st


def page(st):
    url = f"{SITE}/{st['slug']}/"
    others = [o for o in STORES + [CARD_GUIDE] if o is not st]
    ld = {
        "@context": "https://schema.org",
        "@graph": [
            {"@type": "WebPage", "@id": url, "url": url, "name": st["title"],
             "description": st["desc"], "inLanguage": "en-IN",
             "isPartOf": {"@id": f"{SITE}/#site"}},
            {"@type": "FAQPage", "@id": url + "#faq",
             "mainEntity": [{"@type": "Question", "name": q,
                             "acceptedAnswer": {"@type": "Answer", "text": strip(a)}} for q, a in st["faq"]]},
            {"@type": "BreadcrumbList", "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "BlinkDeal", "item": f"{SITE}/"},
                {"@type": "ListItem", "position": 2, "name": st["label"], "item": url}]},
        ],
    }
    how = "\n".join(f"    <li><b>{h}.</b><span> {t}</span></li>" for h, t in st["how"])
    checks = "\n".join(f"    <li><b>{h}.</b> {t}</li>" for h, t in st.get("checks", CHECKS))
    faq = "\n".join(f"    <dt>{q}</dt>\n    <dd>{a}</dd>" for q, a in st["faq"])
    more = "\n".join(f'    <a href="../{o["slug"]}/">{o["label"]}</a>' for o in others)
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{html.escape(st['title'] if 'BlinkDeal' in st['title'] else st['title'] + ' – BlinkDeal')}</title>
<meta name="description" content="{html.escape(st['desc'])}">
<link rel="canonical" href="{url}">
<meta name="theme-color" content="#fbf8f1" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#0e0c09" media="(prefers-color-scheme: dark)">
<meta property="og:type" content="article">
<meta property="og:site_name" content="BlinkDeal">
<meta property="og:locale" content="en_IN">
<meta property="og:url" content="{url}">
<meta property="og:title" content="{html.escape(st['title'])} ⚡ BlinkDeal">
<meta property="og:description" content="{html.escape(st['desc'])}">
<meta property="og:image" content="{SITE}/og-image.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:image" content="{SITE}/og-image.jpg">
<link rel="icon" href="../favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="../apple-touch-icon.png">
<link rel="preconnect" href="https://rsms.me/">
<link rel="stylesheet" href="https://rsms.me/inter/inter.css">
<link rel="stylesheet" href="../page.css">
<script type="application/ld+json">
{json.dumps(ld, ensure_ascii=False, indent=2)}
</script>
<script>
  (function () {{
    var m = matchMedia("(prefers-color-scheme: dark)"), d = document.documentElement;
    function set() {{ d.setAttribute("data-theme", m.matches ? "dark" : "light"); }}
    set();
    if (m.addEventListener) m.addEventListener("change", set);
  }})();
</script>
</head>
<body>
<!-- Generated by tools/guides.py - edit there, not here. -->
{DEFS}{TOPBAR}

<main>
  <p class="crumbs"><a href="../">BlinkDeal</a> › {st['label']}</p>
  <div class="store-hero">
    <img src="{st['icon']}" alt="">
    <p class="eyebrow" style="margin:0">{st['eyebrow']}</p>
  </div>
  <h1>{st['h1']}</h1>
  <p class="lede">{st['lede']}</p>

  <p class="cta" style="margin:0 0 10px;text-align:left"><a class="store-cta" data-store="{st['track']}" href="{st['cta_url']}">⚡ {st['cta_text']}</a></p>

  <h2>{st['how_h']}</h2>
  <ol class="steps">
{how}
  </ol>

  <h2>Is it a good deal? Four things to check</h2>
  <ul class="ticks">
{checks}
  </ul>
  <p class="note">The board does these sums for every piece: what you pay, what the gold in it is worth at the rate you pick, and the gap between the two.</p>

  <h2>{st['faq_h']}</h2>
  <dl>
{faq}
  </dl>

  <h2>More gold deal guides</h2>
  <div class="guides">
{more}
    <a href="../about/">About BlinkDeal</a>
  </div>

  <p class="cta"><a class="store-cta" data-store="{st['track']}" href="{st['cta_url']}">⚡ {st['cta_text']}</a></p>
  <p class="note">Data points, not investment advice. Buy links on the boards may be affiliate links; a small commission may be earned at no extra cost to you.</p>
</main>

{FOOTER}

<script src="../analytics.js"></script>
</body>
</html>
"""


def main():
    for st in STORES:
        store_defaults(st)
    for st in STORES + [CARD_GUIDE]:
        d = os.path.join(ROOT, st["slug"])
        os.makedirs(d, exist_ok=True)
        with open(os.path.join(d, "index.html"), "w", encoding="utf-8", newline="\n") as f:
            f.write(page(st))
        print("wrote", st["slug"])

    urls = [("", "1.0"), ("about/", "0.8")] + [(s["slug"] + "/", "0.9") for s in STORES + [CARD_GUIDE]]
    body = "\n".join(f"  <url><loc>{SITE}/{u}</loc><lastmod>{TODAY}</lastmod><priority>{p}</priority></url>" for u, p in urls)
    with open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8", newline="\n") as f:
        f.write(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{body}\n</urlset>\n')
    print("wrote sitemap.xml with", len(urls), "urls")


if __name__ == "__main__":
    main()
