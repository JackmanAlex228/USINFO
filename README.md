# United States Information & National FOundation for Transparency (USINFO)

## Overview
The **U**nited **S**tates **I**nformation & **N**ational **FO**undation for Transparency (**USINFO**) is a proposed unified informational framework designed to enhance civic participation and transparency for the user by using a "bottom-up" approach to displaying government information where day-to-day city functions are primarily focused. The goal is to create a free application where citizens can easily patriciate in municipal activities (such as city council meetings or city elections), utilize city services (such as permit processing or recycling information) and, in doing so, understand government activities, policies, and decision-making processes, from city-level to state and federal-level.

## Features
There would be a "base" version of the app which contains four screens and a "city" version of the app with an additional fifth screen. Two RSS screes, two directory screens, and a custom city screen.

### Screen 1: Events RSS
Displays primarily city events, including meetings, forums, upcoming city elections, and other city activities. Could also include state and federal-level activities. The UI elements that convey these events will be chronologically ordered but will also contain UI elements for future events as reminders.

**Note:** This will be the hardest to get info for, with more than 18,000 municipalities in the United States and no known centralized database with API access. This may involve either extensive web scraping or extensive municipal involvment. Much of how this data is collected is in-the-air and, at least in the prototype, I might just make my own database and server for Utah cities (my home state).

### Screen 2: Elections RSS
Unlike the Events RSS, this screen only displays election information. Although UI elements for election announcements in the Events RSS employ similar information (election date, voting locations, and candidates), this screen will be referred to for more detailed information with live updates. This will again employ the "bottom-up" hierarchy, where city-level election information is displayed first.

### Screen 3: City Directory
Displays city officials and departments, as well as their duty and contact information. This directory may include information of officials such as City Council members, the Mayor, and City Manager, and information of city departments such as Public Utilities, Parks & Recreation, and the Sheriffs Office.

### Screen 4: State Directory
Displays state and federal officials and departments in much the same way as the City Directory screen (though preferably with structural visual distinctions to deter confusion). Examples of state-level officials and agencies include state legislators, federal congresspeople, the Governor/Attorney General, Department of Workforce Services, Department of Records and Archives, etc. This will also include federal-level information with information on local offices for such.

### Screen 5: City Functions (Optional)
The key feature for this app is the ability for cities to make their own "skin" of the app, as well as employ a templated button with open-ended features which the city can themselves utilize. May involve utilizing an external service with a web interface which cities can use to build and deploy their features. What features can be used depends on whether they'd actually work. For example, a permit processing feature might be possible, but requires knowledge on how payments for them can be processed in ways cities can easily implement on their own.

The possibility of implementing the City Functions feature with its open-ended intentions in mind could be a major challenge, one which requires thorough research on how cities might approach this features, as well as a tangible commitment to security, maintainability, and decoupling from the app's base features and overall fundamental design.

## Data Sources
Although state and federal-level information is easy to obtain by utilizing pre-exiting sources such as Open States or Legistar, anything city-level will be challenging if the goal is to have a useable base app that anyone can use regardless of whether their city employed the City Functions feature. Data scrapping might be necessary.

## Tech Stack
As of the latest commit, these are the planned languages and technologies that might be used:

### Frontend/Client
SwiftUI, Kotlin, and VueJS

### Backend/Server
Python and Django

### Database
SQLite or MongoDB (TBD)

### APIs
REST or GraphQL (TBD)

### DevOps & Deployment
CI/CD with GitHub or Gitlab, App Store/Play Store Deployment (TBD)