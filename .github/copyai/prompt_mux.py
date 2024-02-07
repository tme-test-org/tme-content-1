import requests
import json
import time
import sys
import os
from pdfdocument.document import PDFDocument

api_key = os.getenv('COPYAI_API_KEY')
workflow_id = os.getenv('COPYAI_WF_ID')

url = f"https://api.copy.ai/api/workflow/{workflow_id}/run"


payload = {
	"startVariables": {

####################
### MAIN PROMPT ###
##################    

		"main_prompt": """

        Your output should use the following template:

        ### Summary

        ### Analogy

        ### Notes

        - [Emoji] Bulletpoint

        ### Keywords

        - Explanation

        You have been tasked with creating a concise summary of Transcript.

        Make a summary of the transcript.

        Additionally make a short complex analogy to give context and/or analogy from day-to-day life from the transcript.

        Create 10 bullet points (each with an appropriate emoji) that summarize the key points or important moments from the video's transcription.

        In addition to the bullet points, extract the most important keywords and any complex words not known to the average reader as well as any acronyms mentioned. For each keyword and complex word, provide an explanation and definition based on its occurrence in the transcription.

        Please ensure that the summary, bullet points, and explanations fit within the 330-word limit, while still offering a comprehensive and clear understanding of the video's content.
        
        """,


##########################
### BACKGROUND PROMPT ###
########################
        
        "background_prompt": """
        
        You are an AI assistant tasked with processing and summarizing diverse transcripts. Your role includes distilling complex information into an accessible format that emphasizes clarity, brevity, and relevance. The content you're working with varies widely in topic, so your responses need to be adaptable and insightful, capturing the essence of the material without loss of critical details.
        
        """,


###################
### Text Input ###
#################
        
        "input": """
        
        hello and welcome everyone to another fantastic episode of altitude and happy New Year to you all I of course I'm Woody Woodworth I'm joined today by a very special guest Brian graceley who is well known in the industry for a bunch of different things he is really the uh director of product strategy at red hat but also known and loved by many as the host and producer of the podcast the cloudcast so Brian welcome oh welcome than thanks for having me on it's uh it's good to be with you and uh you and I did a podcast not too long ago so it's good to be doing this again yeah thanks for coming on the show this is great there's never a dull moment in our industry which is really fun if you're in the podcasting Arena or just into the industry growth and transformation arena being that we're just here in 2024 it's a great time to for for me to kind of First Look Backwards into our industry and think about what was happening a little earlier and then maybe make some predictions and contribute s ome thoughts to what the future future holds and pretends for for the cloud industry so one of the things that we haven't really talked about on this show is the trajectory of cloud in terms of its fundamental business model and what I mean about that is you know anyone who's been paying attention who hasn't lived under Iraq in the last couple of years knows that cloud exploded in 2020 and 2021 due to covid and work from home and all of the digitization and migration of workloads it was healthy before that but that really made a big difference in the industry there was a rush to capitalize on cloud Brian do you think that what I call the Great Migration to cloud is starting to to tail off yeah it's a great question I think we're seeing not so much that the cloud is you know is s sort of become its worst enemy so it's slowing down but I think we're just seeing the kind of rationalization that we you know getting getting back to you know what we saw preco which was really do things make sense in the cloud right so from a from from purely an economic perspective we've seen so many companies talk about they have been you know trying to normalize their spend rationalize their spend so you know did all those workloads make sense in the cloud or did we just do it because you know it didn't make sense at the time to have people go into Data Centers and risk their health and all that sort of stuff you know and and I think the other piece of it is we get into you know more and more use cases that are maybe they make sense at the edge maybe they still make sense in the data center we've seen uh you know skill sets improve and Technology improved such that you know some of that scalability that you could you previously could only do in the cloud you can now you know doing your data center you you're using a kubernetes or using other you know other types of Technologies so I don't know if we're so much getting to like Peak migrate to the cloud but I think we're getting to more o f a rationalization that people were like look you know I had to do what I had to do when Co happened we had to keep our businesses running we had to keep people employed all those types of you know real life you know basic survival level things and now you know the economy is a little different the interest rates are a little different than they were previously and and so you know just the reality of of the bottom line the reality of of uh you know just business 101 is kicking in yeah do you th ink cloud providers are doing enough to help control spend I mean I know there's both macro and microeconomic factors that have led to people re-evaluating the amount of spin they have in cloud and it's not I'm not trying to point the finger at at the big csps and say your business model out of whack but they have to respond just like everyone else you know to to the economy and for example I think to the news yesterday and and even this morning I saw more layups at AWS and and Google so the the bloodletting kind of continues smaller than we saw last year are they realizing that they need to tighten the belt a little bit for their customers or are they kind of just putting blinders on and saying ah business is usable I don't want to sort of speculate as as to how they think about things I think the reality with the cloud providers is for the most part as much as we we like to compare them so we'll compare Amazon and Azure and Google or or whoever it might be you know they're they're st ill fundamentally sort of a small oligopoly in terms of you know that there really is only a few of them obviously they they keep a very tight watch on each other so you don't really see you know wildly different cost you know compute from one to the other they're all basically within a within a range but for the most part you know part of their business model is designed around the idea of while they talk about being you know incredibly sort of customer focused and customer friendly and they've at are applicable to certain things right so for example you've seen a lot of the cloud providers roll out arm-based CPUs right so the ability to do you know lower cost CPU but but that doesn't come for free right you still have to make sure your application can use that CPU um you know so so there are some aspects like that you've seen customers get smart and say things like well do I need five replicas of a data set maybe I only need three replicas of a data set or you know other real low-leve by the cloud providers if somebody really wanted to be aggressive so for example if just as an example if you were Google and you said hey I'm tired of being number three I want to be much more aggressive in in try to attract customers and I'm going to try and be visible about we are going to be less expensive but we're also going to be more active in helping you do that they could go about doing that there are things they could be doing if they wanted to be aggressive about doing this it just y t ready for cloud you weren't interested in it or the data was simply too hard to move like it just ran better on Prim but I think they are banking on AI and not just generative AI but all the different facets of AI and machine learning to drive the next wave of what they hope to be migrations would you agree with that well I think it's definitely AI is definitely the thing that you know has has over the last year just sort of exploded in terms of people's interest and and AI is interesting beca oth Topline and bottom line things in terms of AI and so the cloud providers because there's so much Unknown about what a what AI could do for you right good and bad they're rushing like crazy to make sure that when this next Gold Rush happens when the next you know possibilities happen they're they're there and waiting for it so yeah I think they are they're all betting on it you know the good news for them is to a certain extent it feels like an incremental lift of things like gpus and other s d the you know the the the websites that are tracking infrastructure it's pretty obvious that they are doubling tripling down on closing in on being the top providers and hosters I guess for lack of a better term of AI chips so of course there's you know the 800 pound gorilla Nvidia but I think what's happening is very similar to what happened to regular Merchant silicon and x86 in Cloud maybe five or six years ago which is they get tired of paying Nvidia their juicy profits they big shops they' the Glory Days if you will right but maybe this migration will look different maybe the edge is where things will really blow up and and this is looking at AI holistically not as just you know gen AI which is obviously very consumer focused tool and still very young but just all of the facets that AI can be used for in terms of intelligent vehicles intellig sensors aing and Manufacturing everything that's happening in the workplace I'm just curious about your thoughts on this maybe it's not goin t it was essentially you know it was same sort of storage for the most part yes object came along but it was it was storage in compute networking and SQL databases and ethernet and IP so there wasn't like some radically new technology right so the ability to say hey what I used to do in one place I could replicate in the cloud was was pretty straightforward and then I got all the benefits of it moving fast and On Demand and and API driven and so forth AI is sort of different in that it does have ata center and your your article you know smartly points out like the edge is this whole new sort of thing so I think we're going to go through an interesting transition whereas and we've seen this with networking you guys see this all the time like the Next Generation doesn't mean the last generation of networking is just going to follow immediately right we went from north and south east and west and all sorts of stuff I I say this all the time I feel like AI is sort of the the killer applicat opy I think things with AI will get more complicated at an infrastructure level at a user experience level the promise of AI is it's drastically more efficient and in some ways simple because you can get so much information and experience from this one chat interface or this one app but the infrastructure that's going to be built I think is going to summon a new wave of Architects and Security Professionals and experts to do this and I think there might even be people that just focus their caree and everybody got very efficient of running their data centers then we sort of said well let's let's make developers smarter like more efficient and we built microservices and we've done some stuff with containers and kubernetes and while you could point to saying hey you can build an application faster you can deploy it faster like the economic benefit of it was sort of not always super super obvious in some cases it was more obvious so that was more of kind of a drift right AI is one of those ample there's llama 2 that's is that an open source one yes that's uh that's a open source that came out of Facebook okay okay the trend will be towards more diversification and I remember that Wall Street Journal article mentioned that um people are pursuing applications it you know it it wasn't super specific about the architecture but probably from an API perspective they could almost shift not on the fly but pretty close like ha for AI so chat GPT for example hypothetically doesn't perform c e the ansible project that tons of people use for automation of lots of things networking Security Storage OS and so forth you know the anible project uh has been working you know how do I take this Corpus of of knowledge in the community right all these playbooks that have been built before and essentially applied a large language model to that and basically said hey you know if you want to use this tool and in this case it's anible to do some sort of thing you know why are you sort of doing it 20002 2001 yeah we all thought that pets. com was gonna was gonna deliver our dog food for us yes and eventually it it did right I mean a lot of those early ideas came to fruition but it took a bit longer to work out and we had to kind of wait for some of the technology to develop to be able to to deliver on that expectation I'm not saying that AI is going to be subject to vicious boom and bus Cy Cycles because I think like you said it's a paradigm shift we've discussed this on our previous uh p we'll see in with AI is you know like we've seen what like we saw with Cloud for example so so the things that work with Cloud immediately that were successful were I'm going to try and do things natively I'm not going to try and force some old thing onto it right so you know technology when it's early is always built for you know a few use cases you know a few things to do well so you know we'll see people try and force some weird Legacy type of model or framework or something onto Ai and they l happen um you know the the other things are are going to be some of the stuff you talked about like which model do I pick do I pick like a like a like a discussion that we've been having quite a bit and I think the industry is having is you know do I pick the do I pick the one one model that that solves all my problems so just as an example open AI is sort of positioning themselves as you know we have one model for everything you want to you want to write code you want to generate images you w ervice with a you know chat GPT thing so when you show up at the hotel 11 o'clock at night and you're tired and you're like hey what's the best place to order pizza you don't have to worry if you ding the Bell if the person comes out if they're you know doing like you'll see little things like that and then you're going to see big stories like hey this this mining company has figured out a way to be 50% more efficient to drilling holes to find energy or something like that so right I think peopl d on the services that that Drive the revenue as opposed to services that they're like every business they're like every business and you can't you can't slide over that but then some new things too where we might see an explosion of edge um we might see some new architectures we I agree we'll certainly see some roles in some people focusing their careers specifically on AI and then hopefully we'll see like you said small incremental improvements in just our daily lives but then these moments ce should have learned over the last 10 years of how to do Cloud how to do things on demand yes how to have integrated you know development infrastructure teams those types of things so yes you'll have some oneoff teams go off and do something successful with cloud or with AI but if you want to do AI at sort of scale make sure that you know you're you're good at finops you're good at devops you're good at you know the things that that came before it make sure your your foundation
        
        """
	},
	"metadata": {"api": True}
}
headers = {
	"Content-Type": "application/json",
    "x-copy-ai-api-key": api_key
}

response = requests.post(url, json=payload, headers=headers)


# Parse the response text to a dictionary
response_dict = json.loads(response.text)

if 'data' in response_dict:
    if 'id' in response_dict['data']:
        print("Workflow Run ID: " + response_dict['data']['id'])
    else:
        print("'id' not found in 'data'.")
else:
    print("'data' not found in the response.")


# Extract the run_id
run_id = response_dict['data']['id']

# Create the URL for tracking the workflow run
track_url = f"https://api.copy.ai/api/workflow/{workflow_id}/run/{run_id}"

# Track the response
track_response = requests.get(track_url, headers=headers)


while True:
    track_response = requests.get(track_url, headers=headers)
    track_response_dict = json.loads(track_response.text)

    if 'data' in track_response_dict:

        if 'status' in track_response_dict['data']:
            sys.stdout.write('\r' + "Status: " + track_response_dict['data']['status'] + "...")
            sys.stdout.flush()

        # Wait for the status to change to 'COMPLETE' and print the output
        if track_response_dict['data']['status'] == 'COMPLETE':
            output_dict = track_response_dict['data']['output']
            if 'use_prompt_input' in output_dict:
                print("\n\n")
                # print("\n\n##############################")
                # print("########### OUTPUT ###########")
                # print("##############################")
                print(output_dict['use_prompt_input'])



                content = output_dict['use_prompt_input']

### MD Generation ###
                with open("output.md", "w") as f:
                    # Add the content to the Markdown file
                    f.write(content)


### PDF GENERATION ###

                # Create a new PDF document
                pdf = PDFDocument("output.pdf")

                # Add the content to the PDF document
                pdf.init_report()
                pdf.h2('Output')
                pdf.p(content)

                # Save the PDF document
                pdf.generate()

                #print("Output saved to output.pdf")

            else:
                print("'use_prompt_input' not found in 'output'.")
            break

    else:
        print("'data' not found in the response.")

    time.sleep(5)