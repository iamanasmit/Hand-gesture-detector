from src.pipeline.stage1_prepare_model import CreateModelPipeline
from src.pipeline.stage2_preprocess_data import PreprocessPipeline
from src.pipeline.stage3_predict import PredictPipeline

create_model_obj=CreateModelPipeline()
create_model_obj.main()
print('model created')

preprocess_data_obj=PreprocessPipeline()
preprocess_data_obj.main()
print('data preprocessed and stored in pkl format')

predictobj=PredictPipeline()
predictobj.main()