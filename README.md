# python-pact-show-n-tell
A repository for exploring and learning Pact testing between Flask services in a (hopefully) convenient dockerized bundle. I created this repository as a personal project to familiarize myself with Pact testing. Feel free to make suggestions and help me learn!

## Try it yourslef
Pull down the repository in an environment with docker and run `docker-compose up` in the root directory. I recommend then pulling up both the Consumer and Provider in two different windows of your favorite editor. The two different directories are meant to simulate two Flask services running in a networked environment. In this case they are accessible on localhost:3000 and localhost:3001. The dockerfiles for each service include setting up environments, so feel free to run commands either in the containers or in a virtual environment for whichever service you are working with currently.

To test the Pact interaction in the Consumer, run `python -m unittest [path_to_consumer_test_file].test_pact`. You should see two directories generate at the top level, one for logs, and one for Pact files that are being generated. This simulates sending Pacts to a third party for fetching from the Provider service.

To verify the Provider is honoring the Pacts, run `pact-verifier --provider-base-url=http://localhost:3000 --pact-url=[path_to_pact_file]/consumer-provider.json` you should see no failures in the interaction! 

That's pretty much it! This is a rough first pass at getting the tests to actually go, so check back often for more examples and better architecture as I learn more.
