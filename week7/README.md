# Homework 7

* my app is [here](https://chiaki-othello.appspot.com/)

* evaluate the second (=next) state of the board.
* todo: something for further steps ahead.


# Using reflector.go

You can use this "reflector" program to make a locally running dev_appserver instance act like a human player (i.e. you don't have to deploy the whole app to have it run a game).

To run it:
* [download](https://golang.org/dl/) and install Go if you don't have it already.
* Start a new game on https://step-othello.appspot.com with a "Human (or Local bot)" selected as one of the players
* copy the URL of that browser tab showing that game (i.e. a URL that looks like "https://step-othello.appspot.com/view?gamekey=fOoBaR")
* type `go run reflector.go "https://step-othello.appspot.com/view?gamekey=fOoBaR"`
    * (but pasting your actual viewer URL there -- fOoBaR is not a real game ;)
