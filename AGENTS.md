# Repository Guidelines

## Project Structure & Note Organization

This repository is an Obsidian vault for psychology coursework, written primarily in Indonesian. Work under `College 101/`:

- `Zettelkasten/Literature Notes/` contains course-specific lecture notes, assignments, reviews, and drafts.
- `Zettelkasten/Permanent Notes/` contains atomic concept notes.
- `Zettelkasten/MOC/` contains maps of content that organize related notes.
- `Templates/` provides note scaffolding. Use `Core Templates.md` only for Permanent Notes.
- `Assets/` and `Refrences/` store images, diagrams, books, and other source material. Preserve the existing `Refrences` spelling.

Keep attachments near the established asset location and use relative Obsidian links so the vault remains portable.

## Development and Validation Commands

There is no build system or automated test suite. Open the repository as an Obsidian vault for normal editing and visual verification. Before submitting changes, run:

```bash
git status --short            # review changed and untracked files
git diff --check              # detect whitespace errors
git diff --stat               # confirm the scope of the change
rg '\[\[[^]]+\]\]' 'College 101'  # inspect wikilink usage
```

In Obsidian, verify that new links resolve, images render, and headings appear correctly in the outline.

## Writing Style & Naming Conventions

Use Markdown with one top-level title per note and descriptive sentence-case headings below it. Permanent Notes should cover one concept and retain the template metadata fields: `Date`, `Time`, `Status`, `Subject`, and `Tags`. Name notes by their concept, for example `Working Memory.md`; follow the existing course folder and filename patterns for Literature Notes. Connect concepts with `[[Note Name]]` wikilinks, especially in the `# References` section.

Write academic material in concise Indonesian unless the surrounding document uses another language. Use APA style for academic citations. Do not use em dashes.

## Testing and Content Review

Review factual claims, citations, tables, and attachment paths manually. For PDFs, inspect the text layer with `pdf-inspector detect <file> --json` before extraction or OCR. Visually verify tables because automated extraction can reorder columns.

## Commit & Push Guidelines

Recent commits use short, imperative summaries such as `Add footnotes...`, `Update...`, and `Rename...`. Keep each commit focused on one coherent content change. Before pushing, review the staged diff and confirm that wikilinks, citations, and attachments are complete. Push the commit directly to the intended branch. Never commit personal Obsidian workspace state or temporary files covered by `.gitignore`.
