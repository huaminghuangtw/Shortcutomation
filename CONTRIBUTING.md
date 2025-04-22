# 🤝 Contributing to Shortcutomation

Thank you for your interest in contributing to **[Shortcutomation](https://shortcutomation.com)**! 

We welcome new shortcut or automation ideas from the community.

## 📌 How to Contribute

### 🐛 Report Bugs

- Open a [bug report issue](https://github.com/huaminghuangtw/Shortcutomation/issues/new?labels=bug&template=bug-report---.md)
- Include clear steps to reproduce the problem
- Mention your device, OS version, and shortcut name (if relevant)
- Screenshots and GIFs are appreciated!

### 🧠 Suggest a Shortcut

- Open a new [feature request issue.](https://github.com/huaminghuangtw/Shortcutomation/issues/new?labels=enhancement&template=feature-request---.md)
- Clearly describe your idea and the problem it solves.

### 🛠 Submit a Shortcut

0. Before submitting a shortcut, make sure:

- [ ] The shortcut runs normally for everyone without errors.
- [ ] The shortcut is preferably written in **English**.
- [ ] Keep shortcut names readable and descriptive.

1. [Fork the repository](https://github.com/huaminghuangtw/Shortcutomation/fork).

2. Checkout a new branch.

3. Create a JSON file `<yourShortcutName>.json` in the root folder. Follow this format exactly:

```json
{
  "name": "My Awesome Apple Shortcut",
  "icloudLink": "https://www.icloud.com/shortcuts/8d65c606d1924f098b22774de6dc08f8",
  "author": "Hua-Ming Hunag",
  "description": "This is a short description for the shortcut."
}
```

    * `name`: Your shortcut's name
    * `icloudLink`: The iCloud share link for the shortcut
    * `author`: Your name or GitHub username
    * `description`: Briefly describe describe your shortcut and its purpose

4. Commit the modified JSON file.

5. Push your branch to GitHub.

6. [Open a pull request](https://github.com/huaminghuangtw/Shortcutomation/compare).

7. Done! We’ll review your contribution shortly. If needed, we’ll request changes.

## 🙋 Need Help?

Feel free to:

- Browse the [Discussions](https://github.com/huaminghuangtw/Shortcutomation/discussions) and leave your comments.
- Contact [@huaminghuangtw](https://github.com/huaminghuangtw) via GitHub.
- Or just [open a new issue](https://github.com/huaminghuangtw/Shortcutomation/issues/new).

## ⚖️ License Agreement

By submitting a contribution, you agree that your contribution will be licensed under the [MIT License](LICENSE).

This ensures all contributions remain open and freely available for the community.

## 🙌 Thanks

Thanks again for your support and contributions! 🎉

Let’s build something awesome together! ✨
