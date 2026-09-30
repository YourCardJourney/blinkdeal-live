# BlinkDeal

**https://blinkdeal.live** – gold deals, unlocked in a blink.

The front door to the four gold boards: one turning wheel, tap a store, land on its board.

| Store    | Board                                      |
|----------|--------------------------------------------|
| Myntra   | https://blinkdeal.yourcardjourney.store    |
| Amazon   | https://amazongold.yourcardjourney.store   |
| Flipkart | https://flipkartgold.yourcardjourney.store |
| Ajio     | https://ajiogold.yourcardjourney.store     |

A plain static page on GitHub Pages – no build step. Push to `main` and it is live a
minute later.

- Store links and icons: the `PORTALS` list at the top of `app.js`.
- Link preview (WhatsApp, X, Telegram): `og-image.jpg`, drawn from `tools/og.html`.
  Re-render it with `tools\og.cmd` after changing the card.
- Local preview: `python -m http.server 8777` in this folder.

Shared by [@YourCardJourney](https://yourcardjourney.store).
