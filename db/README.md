# Setting up local MySQL server using HomeBrew
Read [this](https://thoughtbot.com/blog/starting-and-stopping-background-services-with-homebrew). 

## Prep: 
- install `brew`  
- install a SQL 'thing' (like `MySQL WorkBench`, ...)  

## 1. install `brew services` via brew (one-time action)
```
brew tap homebrew/services
```

## 2. install `mysql` via `brew` (one-time action)
```
brew install mysql
```

## 3. start a local `mysql` server
In here, `<name of the service> = mysql`.
```
brew services start <name of the service>
```
or 
```
brew services restart <name of the service>
```
Extra, to check what services are running: 
```
brew services list
```
To stop a service: 
```
brew services stop <name of the service>
```
And, if `mysql` is no long exist but u still want to stop the service: 
```
brew services cleanup
```

## 4. checkout MySQL Workbench to see if the local database is 'connect-able'