class Transaction():
    def __init__(self, author: str= "Default author", prompt: str= "A cat in a tree"):
        self.author = author
        self.prompt = prompt
        self.revised_prompt = ''
        self.result_image_url = ''

    def update_result_image_url(self, result_image_url: str):
        self.result_image_url = result_image_url

    def update_revised_prompt(self, revised_prompt: str):
        self.revised_prompt = revised_prompt

    def is_complete(self):
        return bool(self.revised_prompt and self.result_image_url)

    def __repr__(self) -> str:
        return f"Transaction(author='{self.author}', prompt='{self.prompt}', revised_prompt='{self.revised_prompt}', result_image_url='{self.result_image_url}')"
    
    def __str__(self) -> str:
        return f"Transaction by {self.author}"
