# Media — Joule Component

> SAP Fiori for iOS | Joule / Components

## What is it?

A media card is a card container in Joule that displays videos and images.

---

## Rules

**Do:**
- Check supported media formats before using
- Use a URL or alternative approach if the media can't be rendered in a card

**Don't:**
- Show multiple media cards simultaneously (overwhelming)
- Exceed the maximum width

---

## Variations

### Media Card for Images
Displays images in supported formats.

### Media Card for Videos
Displays videos in supported formats. The video must be accessible without further authentication. The original platform's media player (e.g. YouTube) is embedded in the card. Behaviors and controls are defined by that player, limited to within the card.

---

## Error State

If Joule fails to render media content, an `IllustratedMessage` is shown inside the card:
- Unable to load
- Empty URL error

---

## SwiftUI Code Example

```swift
import FioriSwiftUICore

// Image media card
struct JouleMediaCard: View {
    let media: JouleMedia

    var body: some View {
        switch media.type {
        case .image:
            AsyncImage(url: media.url) { image in
                image.resizable().aspectRatio(contentMode: .fit)
            } placeholder: {
                ProgressView().tint(Color.preferredColor(.tintColor))
            }
            .frame(maxWidth: panelMaxWidth)
            .clipShape(RoundedRectangle(cornerRadius: 12))

        case .video:
            // Embed platform player (WKWebView for YouTube etc.)
            VideoPlayerCard(url: media.url)
                .frame(maxWidth: panelMaxWidth, minHeight: 200)
                .clipShape(RoundedRectangle(cornerRadius: 12))

        case .error:
            IllustratedMessage {
                Image(systemName: "exclamationmark.triangle")
                    .foregroundStyle(Color.preferredColor(.criticalLabel))
            } title: {
                Text("Unable to load")
            } description: {
                Text(media.errorMessage ?? "Check the URL and try again.")
            }
        }
    }
}
```

---

## Related

- [illustrated-message.md](illustrated-message.md)
- [object-card.md](object-card.md)
