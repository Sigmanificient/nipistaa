from glob import glob
from pincer import Client
from config import TOKEN


class Bot(Client):

    def __init__(self, token: str):
        super().__init__(token)
        self.load_cogs()

    @Client.event
    async def on_ready(self):
        print("Logged in as", self.bot)

    def load_cogs(self):
        """Load all cogs from the `cogs` directory."""
        for cog in glob("cogs/*.py"):
            self.load_cog(cog.replace("/", ".").replace("\\", ".")[:-3])


if __name__ == "__main__":
    Bot(TOKEN).run()
