# Tech Context: TELOS about Jeff

## Technologies Used

As of the initialization of the memory bank on June 30, 2025, the technical stack for "TELOS about Jeff" is primarily
focused on the full-stack web development portfolio (PJT1), which is a key component of Goal 1 (G1). Other projects
(PJT2 and PJT3) do not yet have finalized technical stacks but will be updated as they progress. Below is the proposed
technology context for PJT1, with placeholders for future projects.

### Full-Stack Web Development Portfolio (PJT1)

- **Frontend**:
  - **React.js**: A JavaScript library for building user interfaces, chosen for its popularity, extensive community
    support, and component-based architecture, which simplifies development for beginners.
  - **CSS Framework (Material-UI or Bootstrap)**: For responsive design and pre-built UI components to speed up frontend
    development and ensure a professional look.
  - **State Management (Redux or Context API)**: To manage application state, particularly for dynamic portfolio content
    like project lists.
- **Backend**:
  - **Node.js**: A JavaScript runtime for server-side development, selected to maintain language consistency across the
    stack, reducing the learning curve.
  - **Express.js**: A lightweight web framework for Node.js, used to build RESTful APIs for managing portfolio data.
- **Database**:
  - **MongoDB**: A NoSQL database chosen for its flexibility with unstructured data, ideal for evolving portfolio
    content. It integrates well with Node.js via libraries like Mongoose.
  - **Mongoose**: An Object Data Modeling (ODM) library for MongoDB and Node.js, simplifying database interactions.
- **Deployment & Hosting**:
  - **Vercel or Netlify**: For frontend hosting, offering free tiers, easy deployment, and CI/CD integration.
  - **Heroku or AWS**: For backend hosting, providing scalable solutions with free or low-cost options for learning
    purposes.
- **Testing**:
  - **Jest**: For unit testing backend APIs, widely used in the JavaScript ecosystem.
  - **React Testing Library**: For testing React components, focusing on user behavior simulation.
- **Version Control**:
  - **Git**: For source code management, essential for tracking changes and collaboration.
  - **GitHub**: As a hosting platform for Git repositories, enabling portfolio publication and version control.

## Development Setup

- **Environment**: Local development on a personal machine (Windows, macOS, or Linux) with Node.js installed (version
  16.x or higher recommended for compatibility with modern packages).
- **IDE**: Visual Studio Code (VSCode) as the primary editor, with extensions for JavaScript, React, and Git integration
  (e.g., ESLint, Prettier, GitLens).
- **Package Manager**: npm (Node Package Manager) for managing dependencies and scripts.
- **Initial Setup Steps for PJT1**:
  1. Install Node.js and npm.
  2. Create a new React app using `npx create-react-app portfolio-frontend`.
  3. Set up a basic Express server with `npm init -y` and `npm install express` in a separate `portfolio-backend`
     directory.
  4. Configure MongoDB locally or use a cloud service like MongoDB Atlas for database setup.
  5. Initialize a Git repository and connect to GitHub for version control.

## Technical Constraints

- **Learning Curve**: Technologies are chosen to minimize complexity for aspiring developers. JavaScript is used across
  the stack to avoid learning multiple languages initially.
- **Cost**: Emphasis on free or low-cost tools (e.g., Vercel free tier, MongoDB Atlas free plan) to ensure accessibility
  for individuals with limited resources.
- **Scalability**: While initial projects are small-scale, the architecture (e.g., REST APIs, cloud hosting) allows for
  scalability if the portfolio grows or attracts more traffic.
- **Time**: Development must fit within personal time constraints, prioritizing quick setup and iterative progress over
  complex setups.

## Dependencies

- **Frontend Dependencies for PJT1**:
  - `react`, `react-dom`, `react-scripts` (core React libraries).
  - Material-UI (`@mui/material`, `@emotion/react`, `@emotion/styled`) or Bootstrap (`bootstrap`, `react-bootstrap`) for
    UI.
  - Optional: `redux` or `react-redux` for state management.
- **Backend Dependencies for PJT1**:
  - `express` for server framework.
  - `mongoose` for MongoDB interaction.
  - Additional utilities like `dotenv` for environment variables, `cors` for cross-origin requests.
- **Testing Dependencies**:
  - `jest` for backend testing.
  - `@testing-library/react`, `@testing-library/jest-dom` for frontend testing.

## Tool Usage Patterns

- **Git Workflow**: Use feature branches for development (e.g., `feature/add-project-page`), commit often with
  meaningful messages following conventional commits, and push to GitHub for backup and showcase.
- **Development Iterations**: Follow an iterative approach—build a minimal viable feature (e.g., static project list),
  test it, deploy it, then enhance (e.g., dynamic data from backend).
- **Testing Practices**: Write tests alongside code development to ensure functionality. Focus on critical paths first
  (e.g., project data retrieval).
- **Deployment Frequency**: Deploy early and often to hosting platforms to validate setups and showcase progress, even
  if it's just a static page initially.

## Future Projects (Placeholders)

- **Quarterly Digital Hygiene Checklist (PJT2)**:
  - **Technologies**: Likely non-technical or minimal tech (e.g., Google Sheets, Notion, or a simple static HTML page
    for checklists).
  - **Setup**: To be determined based on format chosen.
- **Personal Curriculum for Jiu-Jitsu and Emotional Intelligence (PJT3)**:
  - **Technologies**: Potentially static site generators (e.g., Jekyll, Hugo) for a content-focused site, or document
    tools like Markdown with PDF export.
  - **Setup**: To be determined based on delivery method.

This tech context will be updated as projects evolve under "TELOS about Jeff", ensuring that the chosen technologies and
setups align with the project's missions and goals.
