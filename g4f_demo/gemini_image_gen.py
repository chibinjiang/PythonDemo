from g4f.client import Client

client = Client()
response = client.images.generate(
  model="gemini",
  prompt="((masterpiece)),((best quality:1.2)),high resolution,8k,(ultrareal:1.3),(photorealism:1.4),(instagram model, handsome guy:1.2),sharp focus,(mitchellslaggertkm ) photos,((two magicians)),((male and female)) ((boy wearing a magic cloak)),(girl wearing evening dress),((finding a duel with a girl)),(girl standing behind the boy ),(girl looking at boy),(gorgeous),((the background is the lounge)),(((evening))),(((weird))),(((looking at the audience))),<lora :MitchellSlaggertKM:0.8>,",
)
image_url = response.data[0].url

