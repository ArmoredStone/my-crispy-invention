class Transaction():
    def __init__(self, author: str= "Default author", prompt: str= "A cat in a tree"):
        self.author = author
        self.prompt = prompt
        self.revised_prompt = ''
        self.result_image_url = ''

    def __repr__(self) -> str:
        return f"Transaction(author='{self.author}', prompt='{self.prompt}', revised_prompt='{self.revised_prompt}', result_image_url='{self.result_image_url}')"
    
    def __str__(self) -> str:
        return f"Transaction by {self.author}"
    
    def update_revised_prompt(self, revised_prompt: str) -> None:
        """Update the revised prompt for this transaction."""
        self.revised_prompt = revised_prompt
    
    def update_result_image_url(self, image_url: str) -> None:
        """Update the result image URL for this transaction."""
        self.result_image_url = image_url
    
    def is_complete(self) -> bool:
        """Check if the transaction has both revised prompt and result image."""
        return bool(self.revised_prompt and self.result_image_url)
    
    def to_dict(self) -> dict:
        """Convert transaction to dictionary representation."""
        return {
            'id': self.id,
            'author': self.author,
            'prompt': self.prompt,
            'revised_prompt': self.revised_prompt,
            'result_image_url': self.result_image_url,
            'created_at': self.created_at.isoformat(),
        }
