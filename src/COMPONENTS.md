# Components Documentation

This document provides an overview of all components used in the website along with their descriptions, usage, and locations.

## Layout Components

1. **Layout.astro**
   - Location: `/src/layouts/Layout.astro`
   - Purpose: Main layout template used across all pages
   - Components used:
     - NavBar.astro
     - Footer.astro
     - ScrollToTop.astro

## Core Components

1. **NavBar.astro**
   - Location: `/src/components/NavBar.astro`
   - Purpose: Main navigation bar for the website
   - Used in: Layout.astro (appears on all pages)
   - Features: Responsive design, active link highlighting

2. **Footer.astro**
   - Location: `/src/components/Footer.astro`
   - Purpose: Site footer with copyright and contact information
   - Used in: Layout.astro (appears on all pages)

3. **ScrollToTop.astro**
   - Location: `/src/components/ScrollToTop.astro`
   - Purpose: Provides a button to scroll back to the top of the page
   - Used in: Layout.astro (appears on all pages)

4. **FeaturesSection.astro**
   - Location: `/src/components/FeaturesSection.astro`
   - Purpose: Highlights the key offerings of the platform to visitors
   - Used in: index.astro
   
5. **SearchComponent.astro**
   - Location: `/src/components/SearchComponent.astro`
   - Purpose: Provides search functionality for documents
   - Used in: tai-lieu.astro
   
6. **DownloadSection.astro**
   - Location: `/src/components/DownloadSection.astro`
   - Purpose: Displays download options for document resources
   - Used in: documents/[slug].astro

## Home Page Components

All located in `/src/components/home/`

1. **HeroSection.astro**
   - Purpose: Main hero section for the homepage
   - Used in: index.astro

2. **FeaturesGrid.astro**
   - Purpose: Grid display of website features
   - Used in: index.astro

3. **StatsSection.astro**
   - Purpose: Display statistics about the platform
   - Used in: index.astro

4. **DocumentsPreview.astro**
   - Purpose: Preview of recent documents
   - Used in: index.astro

5. **TestimonialsSection.astro**
   - Purpose: Display user testimonials
   - Used in: index.astro

6. **CTASection.astro**
   - Purpose: Call to action section
   - Used in: index.astro

7. **InteractiveDemo.jsx**
   - Purpose: Interactive demo component (React)
   - Used in: index.astro

## Document Components

All located in `/src/components/document/`

1. **FilterSection.astro**
   - Purpose: Provides filtering options for documents
   - Used in: tai-lieu.astro

2. **DocumentGrid.astro**
   - Purpose: Grid display of documents
   - Used in: tai-lieu.astro

3. **DocumentCard.astro**
   - Purpose: Card component for individual document display
   - Used in: DocumentGrid.astro

## UI Components

Located in `/src/components/ui/`

1. **Badge.astro**
   - Purpose: Displays category or type badges
   - Used in: DocumentCard.astro, DocumentsPreview.astro

2. **Button.astro**
   - Purpose: Reusable button component
   - Used in: FilterSection.astro
