from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline

llm = HuggingFacePipeline.from_model_id(
    model_id="Qwen/Qwen2.5-0.5B-Instruct",
    task="text-generation",
    pipeline_kwargs={
        "max_new_tokens": 4,
        "top_k": 30,
        "temperature": 0.7,
        "repetition_penalty": 1.25
    }
)

model = ChatHuggingFace(llm=llm)

result = model.invoke("What is the capital of India?")

print(result.content)

#Python Models/2.ChatModels/3_chatmodel_hf_local.py 