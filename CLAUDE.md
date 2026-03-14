# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## PDF Processing                                                                                                     
For PDFs over 20 pages, split into parallel pdf-reader agents (20 pages each). Collect all extracted content, then pass it to the writing agent to produce the final literature note. For PDFs under 20 pages, use a single pdf-reader agent then pass to the writing agent.

## Repository Overview

This is a personal Zettelkasten knowledge repository for a psychology college student (Rafi Mahadika Sujianto). All notes are written primarily in Indonesian (Bahasa Indonesia), covering college subjects in Psychology.

## Structure

```
College 101/
├── Zettelkasten/
│   ├── Literature Notes/   # Course-specific lecture & assignment notes, organized by subject
│   └── Permanent Notes/     # Atomic concept notes, linked to each other (linked and sourced from literature note for most of the times)
├── Templates/               # Note templates (Core, Book, Daily, Resume)
├── Refrences/Books/         # Book summaries and references
└── Assets/                  # Images and diagrams
```

## Note Types

**Literature Notes** (`Literature Notes/`) — organized by course/subject folder:
- Lecture summaries, task write-ups, journal reviews, drafts

**Permanent Notes** (`Permanent Notes/`) — atomic concept notes:
- One idea per note
- Linked to other notes via `[[Note Name]]` wiki-links
- Uses the Core Template structure

### Resume Template
For lecture summaries — includes `Pertemuan Ke -` (session number) and student identity header. ALWAYS ASK FOR SESSION NUMBER

## Writing Style

- Never use em dashes (—). Use commas, semicolons, colons, parentheses, or other connectors instead.
- Default to APA format for all academic work.

## Linking

Notes use Obsidian-style wiki-links `[[Note Name]]` to connect concepts. Permanent Notes heavily rely on cross-linking. When creating or editing Permanent Notes, add relevant `[[links]]` in the `# References` section.