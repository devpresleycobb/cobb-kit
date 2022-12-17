#Welcome to the CobbKit repository!

CobbKit is a desktop app used to as a base for tools I find helpful. The repo currently contains a single app that connects to GitHub and retrieves pull requests that have not been reviewed.

Please note that this app is a proof of concept and is intended to be improved upon in the future and is not meant for production. As such, it was written quickly and may not adhere to best practices at this time.

To use the app, you will need to create a .env file in the root of the project with the following structure:

```bash
ACCESS_TOKEN=your_personal_access_token
ORG_1=your_first_github_organization
ORG_2=your_second_github_organization
```
Replace `your_personal_access_token` with a personal access token that you have generated from GitHub, and replace `your_first_github_organization` and `your_second_github_organization` with the names of the organizations you want to retrieve pull requests for.

We hope you find this package useful, and we welcome any feedback or contributions to improve it!
