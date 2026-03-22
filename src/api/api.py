import aiohttp

class Api:

    @staticmethod
    async def get_all_posts():

        async with aiohttp.ClientSession() as session:

            async with session.get("http://localhost:8000/graphql?query={news{post{title, previewImage}}}") as resp:

                if resp.status == 200:

                    return await resp.json()
                
                else:

                    raise Exception("coudnt get news...")
                
    @staticmethod
    async def load_photo(imageUrl : str):

        async with aiohttp.ClientSession() as session:

            async with session.get(imageUrl) as resp:

                if resp.status == 200:

                    return await resp.read()
                
                else:

                    raise Exception("coudnt get news...")