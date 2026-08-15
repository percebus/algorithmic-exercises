/**
 * @type {import('semantic-release').GlobalConfig}
 */
export default {
  branches: ["main", "next"],
  plugins: [
    "@semantic-release/commit-analyzer",
    "@semantic-release/release-notes-generator",
    [
      "@semantic-release/changelog",
      {
        changelogTitle: "# algorithmic-exercises CHANGELOG",
      },
    ],
    [
      "@semantic-release/npm",
      {
        npmPublish: false,
        tarballDir: "dist",
      },
    ],
    [
      "@semantic-release/exec",
      {
        prepareCmd: "npm run format",
      },
    ],
    [
      "@semantic-release/git",
      {
        assets: ["package.json", "CHANGELOG.md", "requirements*.txt"],
        changelogFile: "CHANGELOG.md",
      },
    ],
    [
      "@semantic-release/github",
      {
        assets: [{ path: "dist/*.tgz" }],
      },
    ],
  ],
};
