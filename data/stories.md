## happy path
* greet
    - utter_greet
* request_interview
    - interview_form
    - form{"name": "interview_form"}
    - form{"answer_2": "Exit"}
* restart
    - utter_greet

## unhappy path
* greet
    - utter_greet
* request_interview
    - interview_form
    - form{"name": "interview_form"}
* chitchat
    - utter_chitchat
    - interview_form
    - form{"name": null}
    - utter_slots_values
* thankyou
    - utter_noworries

## very unhappy path
* greet
    - utter_greet
* request_interview
    - interview_form
    - form{"name": "interview_form"}
* chitchat
    - utter_chitchat
    - interview_form
* chitchat
    - utter_chitchat
    - interview_form
* chitchat
    - utter_chitchat
    - interview_form
    - form{"name": null}
    - utter_slots_values
* thankyou
    - utter_noworries

## stop but continue path
* greet
    - utter_greet
* request_interview
    - interview_form
    - form{"name": "interview_form"}
* stop
    - utter_ask_continue
* affirm
    - interview_form
    - form{"name": null}
    - utter_slots_values
* thankyou
    - utter_noworries

## stop and really stop path
* greet
    - utter_greet
* request_interview
    - interview_form
    - form{"name": "interview_form"}
* stop
    - utter_ask_continue
* deny
    - action_deactivate_form
    - form{"name": null}

## chitchat stop but continue path
* request_interview
    - interview_form
    - form{"name": "interview_form"}
* chitchat
    - utter_chitchat
    - interview_form
* stop
    - utter_ask_continue
* affirm
    - interview_form
    - form{"name": null}
    - utter_slots_values
* thankyou
    - utter_noworries

## stop but continue and chitchat path
* greet
    - utter_greet
* request_interview
    - interview_form
    - form{"name": "interview_form"}
* stop
    - utter_ask_continue
* affirm
    - interview_form
* chitchat
    - utter_chitchat
    - interview_form
    - form{"name": null}
    - utter_slots_values
* thankyou
    - utter_noworries

## chitchat stop but continue and chitchat path
* greet
    - utter_greet
* request_interview
    - interview_form
    - form{"name": "interview_form"}
* chitchat
    - utter_chitchat
    - interview_form
* stop
    - utter_ask_continue
* affirm
    - interview_form
* chitchat
    - utter_chitchat
    - interview_form
    - form{"name": null}
    - utter_slots_values
* thankyou
    - utter_noworries

## chitchat, stop and really stop path
* greet
    - utter_greet
* request_interview
    - interview_form
    - form{"name": "interview_form"}
* chitchat
    - utter_chitchat
    - restaurant_form
* stop
    - utter_ask_continue
* deny
    - action_deactivate_form
    - form{"name": null}

## Generated Story 3490283781720101690 (example from interactive learning, "form: " will be excluded from training)
* greet
    - utter_greet
* request_interview
    - interview_form
    - form{"name": "interview_form"}
    - slot{"requested_slot": "eid"}
* chitchat
    - utter_chitchat  <!-- restaurant_form was predicted by FormPolicy and rejected, other policy predicted utter_chitchat -->
    - interview_form
    - slot{"requested_slot": "eid"}
* form: inform{"eid": "saicharantej99@gmail.com"}
    - slot{"answer_1": "1:1"}
    - form: interview_form
    - slot{"answer_2": "decrease"}
    - slot{"requested_slot": "answer_2"}
* form: inform{"answer_1": "50:50"}
    - form: interview_form
    - slot{"answer_2": "decrease"}
    - slot{"requested_slot": "answer_3"}
* chitchat
    - utter_chitchat
    - interview_form
    - slot{"requested_slot": "eid"}
* stop
    - utter_ask_continue
* affirm
    - interview_form  <!-- FormPolicy predicted FormValidation(False), other policy predicted restaurant_form -->
    - slot{"requested_slot": "eid"}
* form: affirm
    - form: interview_form
    - slot{"answer_1": "1:1"}
    - slot{"answer_2": "increase"}
* form: inform
    - form: interview_form
    - slot{"answer_2": "decrease"}
    - utter_slots_values
* thankyou
    - utter_noworries

## bot challenge
* bot_challenge
  - utter_iamabot

## New Story

* greet
    - utter_greet
* request_interview
    - interview_form
    - form{"name":"interview_form"}
    - slot{"requested_slot":"eid"}
* inform{"eid":"saicharantej99@gmail.com"}
    - interview_form
    - slot{"eid":"saicharantej99@gmail.com"}
    - slot{"requested_slot":"answer_1"}
* inform
    - action_default_fallback
* inform{"answer_1":"1:1"}
    - interview_form
    - slot{"answer_1":"1:1"}
    - slot{"requested_slot":"answer_2"}
* inform
    - action_default_fallback
* inform{"answer_2":"decrease"}
    - interview_form
    - slot{"answer_2":"decrease"}
    - slot{"requested_slot":"answer_3"}
* inform
    - action_default_fallback
* inform
    - action_default_fallback
* inform{"answer_3":"$905"}
    - interview_form
    - slot{"answer_3":"$905"}
    - form{"name":null}
    - slot{"requested_slot":null}
    - utter_slots_values

## Code Reco1

* greet
    - utter_greet
* code_reco
    - utter_ask_code
* missing_values
    - utter_missing_values
* knn_reco
    - utter_knn
> checkpoint_another_reco

## Code Reco2

* greet
    - utter_greet
* code_reco
    - utter_ask_code

* imbalance_reco
    - utter_imbalance
* smote_reco
    - utter_smote
    - action_restart
* restart
    - utter_ask_code

## Story from conversation with 89aee8f733104e55b23fc0e5d91cea56 on July 27th 2020

* greet
    - utter_greet
* code_reco
    - utter_ask_code
* imbalance_reco{"answer_1":"Class Imbalance"}
    - utter_imbalance
* smote_reco
    - utter_smote

## Code Reco1.1

* code_reco
    - utter_ask_code
* missing_values
    - utter_missing_values
* null_reco
    - utter_null
> checkpoint_another_reco
* restart
    - utter_ask_code

## Code Reco1.2

* code_reco
    - utter_ask_code
* missing_values
    - utter_missing_values
* impute_reco
    - utter_impute
    - action_restart
* restart
    - utter_ask_code

### Outlier Story

* greet
    - utter_greet
* code_reco
    - utter_ask_code
> checkpoint_another_reco
* outlier_reco
    - utter_outliers
    - utter_continue
* restart
    - utter_ask_code

## Punctuation Story
* greet
    - utter_greet
* code_reco
    - utter_ask_code
* special_reco
    - utter_special
* html_reco
    - utter_html
    - utter_continue
* restart
    - utter_ask_code

## Punctuation Story2
* greet
    - utter_greet
* code_reco
    - utter_ask_code
* special_reco
    - utter_special
* punctuation_reco
    - utter_punctuation
    - utter_continue
* restart
    - utter_ask_code

## Code Reco KNN

* greet
    - utter_greet
* code_reco
    - utter_ask_code
* imbalance_reco
    - utter_imbalance
* smote_reco
    - utter_smote
* knn_reco
    - utter_tutorial
    - utter_knn_tutorial
    - utter_continue
* restart
    - utter_ask_code

## Story from conversation with U0182JCBDM0 on July 31st 2020
* greet
    - utter_greet
* code_reco
    - utter_ask_code
* chitchat
    - utter_chitchat
* greet
    - utter_greet
* greet
    - utter_greet
* imbalance_reco
    - utter_imbalance
* metric_reco
    - utter_metric
* cost_reco
    - utter_cost
* smote_reco
    - utter_smote
* chitchat{"answer_1":"Ok grt"}
    - utter_chitchat
    - utter_continue
* restart
    - utter_ask_code

## Poisson Story

* greet
    - utter_greet
* code_reco
    - utter_ask_code
* poisson_reco
    - utter_poisson
    - utter_continue
* restart
    - utter_ask_code

## New Story

* greet
    - utter_greet
* code_reco
    - utter_ask_code
* poisson_reco
    - utter_poisson
    - utter_continue
* restart
    - utter_ask_code

## Encoding Story 1
* greet
    - utter_greet
* code_reco
    - utter_ask_code
* encoding_reco
    - utter_encode
* target_reco
    - utter_frequency
    - utter_meanencoder
    - utter_continue
* restart
    - utter_ask_code

## Encoding Story 2
* greet
    - utter_greet
* code_reco
    - utter_ask_code
* encoding_reco
    - utter_encode
* categorical_reco
    - utter_categorical_reco
* onehot_reco
    - utter_onehot
    - utter_continue
* restart
    - utter_ask_code

## Encoding Story 3
* greet
    - utter_greet
* code_reco
    - utter_ask_code
* encoding_reco
    - utter_encode
* categorical_reco
    - utter_categorical_reco
* categorical_reco
    - utter_categorical_question
* binary_reco
    - utter_binary
    - utter_continue
* restart
    - utter_ask_code

## Encoding Story 4
* greet
    - utter_greet
* code_reco
    - utter_ask_code
* encoding_reco
    - utter_encode
* categorical_reco
    - utter_categorical_reco
* categorical_reco
    - utter_categorical_question
* label_reco
    - utter_label
    - utter_continue
* restart
    - utter_ask_code

## New Story

* greet
    - utter_greet
* code_reco
    - utter_ask_code
* encoding_reco
    - utter_encode
* categorical_reco
    - utter_categorical_reco
* categorical_reco
    - utter_categorical_question
* label_reco
    - utter_label
    - utter_continue
* restart
    - utter_ask_code

## WordCloud Story
> checkpoint_another_reco
* wordcloud_reco
    - utter_wordcloud
    - utter_continue
* restart
    - utter_ask_code

## Stopwordaddremoval Story

* greet
    - utter_greet
* code_reco
    - utter_ask_code
* stopwordaddremoval_reco
    - utter_stopwordaddremoval
* thankyou
    - utter_noworries

## Encoding Story 5

* greet
    - utter_greet
* code_reco
    - utter_ask_code
* encoding_reco
    - utter_encode
* target_reco
    - utter_frequency
    - utter_meanencoder

## New Story

* request_interview
    - interview_form
    - form{"name":"interview_form"}
    - slot{"requested_slot":"eid"}
* inform{"eid":"saicharantej99@gmail.com"}
    - interview_form
    - slot{"eid":"saicharantej99@gmail.com"}
    - slot{"question":"Which of the below activation functions suffer from vanishing gradient?"}
    - slot{"answer":"Tanh"}
    - slot{"answer_2":null}
    - slot{"option_1":"Tanh"}
    - slot{"option_2":"Leaky Relu"}
    - slot{"explanation":"Tanh suffers from vanishing gradient problem just like sigmoid. Leaky Relu on the other hand is resistant to the problem."}
    - slot{"requested_slot":"answer_1"}
* inform{"answer_1":"Ta"}
    - interview_form
    - slot{"answer_1":"Ta"}
    - slot{"question":"Which of the below activation functions suffer from vanishing gradient?"}
    - slot{"option_1":"Tanh"}
    - slot{"option_2":"Leaky Relu"}
    - slot{"explanation":"Tanh suffers from vanishing gradient problem just like sigmoid. Leaky Relu on the other hand is resistant to the problem."}
    - slot{"requested_slot":"answer_2"}
* inform{"answer_2":"value"}
    - interview_form
    - slot{"answer_2":null}
    - slot{"answer_1":null}
    - slot{"question":"Which of the below algorithms does feature engineering implicitly during the training phase?"}
    - slot{"answer":"Neural Networks"}
    - slot{"option_1":"Naive Bayes"}
    - slot{"option_2":"Neural Networks"}
    - slot{"explanation":"All the neuron combinations that you see in a Neural Network - that is feature engineering right there!"}
    - slot{"requested_slot":"answer_1"}
* inform{"answer_1":"Neural Networks"}
    - interview_form
    - slot{"answer_1":"Neural Networks"}
    - slot{"question":"Which of the below algorithms does feature engineering implicitly during the training phase?"}
    - slot{"option_1":"Naive Bayes"}
    - slot{"option_2":"Neural Networks"}
    - slot{"explanation":"All the neuron combinations that you see in a Neural Network - that is feature engineering right there!"}
    - slot{"requested_slot":"answer_2"}
* inform{"answer_2":"value"}
    - interview_form
    - slot{"answer_2":null}
    - slot{"answer_1":null}
    - slot{"question":"Which of the below values can be part of the ‘criterion’ hyperparameter in a decision tree?"}
    - slot{"answer":"Gini"}
    - slot{"option_1":"Information gain"}
    - slot{"option_2":"Gini"}
    - slot{"explanation":"Gini Index is the name of the criterion that lets you calculate the information gain while building a decision tree. You do not have a hyperparameter by the name 'Information Gain'."}
    - slot{"requested_slot":"answer_1"}

## Line chart using matplotlib

* greet
    - utter_greet
* code_reco
    - utter_ask_code
* data_visualization_reco
    - utter_data_visualization
* linechart_reco{"answer_1":"Linechart"}
    - utter_linechart
* linechart_code_reco{"answer_1":"Code for Linechart"}
    - utter_ask_code1
* linechart_matplotlib_reco
    - utter_linechart_matplotlib    
* thankyou
    - utter_noworries

## Line chart using Seaborn

* greet
    - utter_greet
* code_reco
    - utter_ask_code
* data_visualization_reco
    - utter_data_visualization
* linechart_reco{"answer_1":"Linechart"}
    - utter_linechart
* linechart_code_reco{"answer_1":"Code for Linechart"}
    - utter_ask_code1
* linechart_seaborn_reco
    - utter_linechart_seaborn   
* thankyou
    - utter_noworries

## Line chart using Bokeh

* greet
    - utter_greet
* code_reco
    - utter_ask_code
* data_visualization_reco
    - utter_data_visualization
* linechart_reco{"answer_1":"Linechart"}
    - utter_linechart
* linechart_code_reco{"answer_1":"Code for Linechart"}
    - utter_ask_code1
* linechart_bokeh_reco
    - utter_linechart_bokeh   
* thankyou
    - utter_noworries

## Line chart using Plotly

* greet
    - utter_greet
* code_reco
    - utter_ask_code
* data_visualization_reco
    - utter_data_visualization
* linechart_reco{"answer_1":"Linechart"}
    - utter_linechart
* linechart_code_reco{"answer_1":"Code for Linechart"}
    - utter_ask_code1
* linechart_plotly_reco
    - utter_linechart_plotly   
* thankyou
    - utter_noworries

## Line chart using Ggplot

* greet
    - utter_greet
* code_reco
    - utter_ask_code
* data_visualization_reco
    - utter_data_visualization
* linechart_reco{"answer_1":"Linechart"}
    - utter_linechart
* linechart_code_reco{"answer_1":"Code for Linechart"}
    - utter_ask_code1
* linechart_ggplot_reco
    - utter_linechart_ggplot   
* thankyou
    - utter_noworries

## Bar chart using matplotlib

* greet
    - utter_greet
* code_reco
    - utter_ask_code
* data_visualization_reco
    - utter_data_visualization
* barchart_reco{"answer_1":"Bar Chart"}
    - utter_barchart
* barchart_code_reco{"answer_1":"Code for Bar Chart"}
    - utter_ask_code2
* barchart_matplotlib_reco
    - utter_barchart_matplotlib    
* thankyou
    - utter_noworries

## Bar chart using seaborn

* greet
    - utter_greet
* code_reco
    - utter_ask_code
* data_visualization_reco
    - utter_data_visualization
* barchart_reco{"answer_1":"Bar Chart"}
    - utter_barchart
* barchart_code_reco{"answer_1":"Code for Bar Chart"}
    - utter_ask_code2
* barchart_seabron_reco
    - utter_barchart_seaborn   
* thankyou
    - utter_noworries

## Bar chart using plotly

* greet
    - utter_greet
* code_reco
    - utter_ask_code
* data_visualization_reco
    - utter_data_visualization
* barchart_reco{"answer_1":"Bar Chart"}
    - utter_barchart
* barchart_code_reco{"answer_1":"Code for Bar Chart"}
    - utter_ask_code2
* barchart_plotly_reco
    - utter_barchart_plotly 
* thankyou
    - utter_noworries

## Bar chart using ggplot

* greet
    - utter_greet
* code_reco
    - utter_ask_code
* data_visualization_reco
    - utter_data_visualization
* barchart_reco{"answer_1":"Bar Chart"}
    - utter_barchart
* barchart_code_reco{"answer_1":"Code for Bar Chart"}
    - utter_ask_code2
* barchart_ggplot_reco
    - utter_barchart_ggplot   
* thankyou
    - utter_noworries

## Bar chart using seaborn

* greet
    - utter_greet
* code_reco
    - utter_ask_code
* data_visualization_reco
    - utter_data_visualization
* barchart_reco{"answer_1":"Bar Chart"}
    - utter_barchart
* barchart_code_reco{"answer_1":"Code for Bar Chart"}
    - utter_ask_code2
* barchart_bokeh_reco
    - utter_barchart_bokeh   
* thankyou
    - utter_noworries

## Histogram using seaborn

* greet
    - utter_greet
* code_reco
    - utter_ask_code
* data_visualization_reco
    - utter_data_visualization
* histogram_reco{"answer_1":"Histogram"}
    - utter_histogram
* histogram_code_reco{"answer_1":"Code for Histogram"}
    - utter_ask_code3
* histogram_seabron_reco
    - utter_histogram_seaborn   
* thankyou
    - utter_noworries

## Histogram using ggplot

* greet
    - utter_greet
* code_reco
    - utter_ask_code
* data_visualization_reco
    - utter_data_visualization
* histogram_reco{"answer_1":"Histogram"}
    - utter_histogram
* histogram_code_reco{"answer_1":"Code for Histogram"}
    - utter_ask_code3
* histogram_ggplot_reco
    - utter_histogram_ggplot   
* thankyou
    - utter_noworries

## Histogram using bokeh

* greet
    - utter_greet
* code_reco
    - utter_ask_code
* data_visualization_reco
    - utter_data_visualization
* histogram_reco{"answer_1":"Histogram"}
    - utter_histogram
* histogram_code_reco{"answer_1":"Code for Histogram"}
    - utter_ask_code3
* histogram_bokeh_reco
    - utter_histogram_bokeh   
* thankyou
    - utter_noworries

## Histogram using matplotlib

* greet
    - utter_greet
* code_reco
    - utter_ask_code
* data_visualization_reco
    - utter_data_visualization
* histogram_reco{"answer_1":"Histogram"}
    - utter_histogram
* histogram_code_reco{"answer_1":"Code for Histogram"}
    - utter_ask_code3
* histogram_matplotlib_reco
    - utter_histogram_matplotlib   
* thankyou
    - utter_noworries

## Histogram using plotly

* greet
    - utter_greet
* code_reco
    - utter_ask_code
* data_visualization_reco
    - utter_data_visualization
* histogram_reco{"answer_1":"Histogram"}
    - utter_histogram
* histogram_code_reco{"answer_1":"Code for Histogram"}
    - utter_ask_code3
* histogram_plotly_reco
    - utter_histogram_plotly  
* thankyou
    - utter_noworries

## New Story

* code_reco
    - action_default_fallback
* barchart_reco{"answer_1":"barchart"}
    - action_default_fallback

## Model Explain Story 1
* greet
    - utter_greet
* code_reco
    - utter_ask_code
* model_explain
  - utter_model_explain
* lime
  - utter_lime
* shap
  - utter_shap
* eli5
  - utter_eli5

## Checkpoint Story 1
* greet
    - utter_greet
* code_reco
    - utter_ask_code
* checkpoint
  - utter_checkpoint4

## Tensorboard Story 1
* greet
  - utter_greet
* code_reco
  - utter_ask_code
* tensorboard
  - utter_tensorboard

## Stemming Story
* greet
    - utter_greet
* code_reco
    - utter_ask_code
* stem_dn
  - utter_stem_dn
* stem_words
  - utter_words
* stem_sentence
  - utter_sentence
* affirm
  - utter_happy

## Optimizer BGD Story
* greet
    - utter_greet
* code_reco
    - utter_ask_code
* optimizer
    - utter_optimizer
* bgd
    - utter_bgd

## Optimizer SGD Story
* greet
    - utter_greet
* code_reco
    - utter_ask_code
* optimizer
    - utter_optimizer
* sgd
    - utter_sgd

## Optimizer MBGD Story
* greet
    - utter_greet
* code_reco
    - utter_ask_code
* optimizer
    - utter_optimizer
* mbgd
    - utter_mbgd

## Optimizer Momentum Story
* greet
    - utter_greet
* code_reco
    - utter_ask_code
* optimizer
    - utter_optimizer
* momentum
    - utter_momentum

## Optimizer Adagrad Story
* greet
    - utter_greet
* code_reco
    - utter_ask_code
* optimizer
    - utter_optimizer
* adagrad
    - utter_adagrad

## Optimizer Adadelta Story
* greet
    - utter_greet
* code_reco
    - utter_ask_code
* optimizer
    - utter_optimizer
* adadelta
    - utter_adadelta

## Optimizer RMSprop Story
* greet
    - utter_greet
* code_reco
    - utter_ask_code
* optimizer
    - utter_optimizer
* rmsprop
    - utter_rmsprop

## Optimizer Adam Story
* greet
    - utter_greet
* code_reco
    - utter_ask_code
* optimizer
    - utter_optimizer
* adam
    - utter_adam

## Curse of Dimensionality Story
> checkpoint_another_reco
* curse_of_dimensionality_reco
    - utter_cod
* pca_reco
    - utter_pca

## Curse of Dimensionality LDA Story
* greet
    - utter_greet
* code_reco
    - utter_ask_code
* curse_of_dimensionality_reco
    - utter_cod
* lda_reco
    - utter_lda

## NER Story
* greet
    - utter_greet
* code_reco
    - utter_ask_code
* ner_dn
    - utter_ner_dn
* stem_ner
    - utter_ner

## CNER Story
* greet
    - utter_greet
* code_reco
    - utter_ask_code
* ner_dn
    - utter_ner_dn
* stem_cner
    - utter_cner

## Stemming word Story
> checkpoint_another_reco
* stem_reco
    - utter_stem
* stem_word_reco
    - utter_stem_word

## Stemming sentence Story
> checkpoint_another_reco
* stem_reco
    - utter_stem
* stem_sentence_reco
    - utter_stem_sentence

## Code Reco1 Duplicate

* code_reco
    - utter_ask_code
* missing_values
    - utter_missing_values
* knn_reco
    - utter_knn
    - action_restart
* restart
    - utter_ask_code

## Code Reco2 Duplicate

* code_reco
    - utter_ask_code
* imbalance_reco
    - utter_imbalance
* smote_reco
    - utter_smote
    - action_restart
* restart
    - utter_ask_code

## Code Reco1 Duplicate

* code_reco
    - utter_ask_code
* missing_values
    - utter_missing_values
* knn_reco
    - utter_knn
    - action_restart
* restart
    - utter_ask_code

## Code Reco2 Duplicate

* code_reco
    - utter_ask_code
* imbalance_reco
    - utter_imbalance
* smote_reco
    - utter_smote
    - action_restart
* restart
    - utter_ask_code

## Wordcloud Story
> checkpoint_another_reco
* wordcloud_reco
    - utter_wordcloud

## New Story training Outlier Word Cloud

* greet
    - utter_greet
* code_reco
    - utter_ask_code
* outlier_reco
    - utter_outliers
    - utter_continue
* code_reco
    - utter_ask_code
* wordcloud_reco
    - utter_wordcloud

## Duplicate rows

* greet
    - utter_greet
* code_reco
    - utter_ask_code
* duplicate_reco
    - utter_duplicate

## Cost Function

* greet
    - utter_greet
* code_reco
    - utter_ask_code
* imbalance_reco
    - utter_imbalance
* cost_reco
    - utter_cost

## Imbalance and Outliers

* greet
    - utter_greet
* code_reco
    - utter_ask_code
* encoding_reco
    - utter_encode
* categorical_reco
    - utter_categorical_reco
* categorical_reco
    - utter_categorical_question
* label_reco
    - utter_label
    - utter_continue
* code_reco
    - utter_ask_code
* outlier_reco
    - utter_outliers

## WordCloud and Missing Values

* code_reco
    - utter_ask_code
* wordcloud_reco
    - utter_wordcloud
* missing_values
    - utter_missing_values
* impute_reco
    - utter_impute

## Pie chart using Bokeh

* greet
    - utter_greet
* code_reco
    - utter_ask_code
* data_visualization_reco
    - utter_data_visualization
* Piechart_reco{"answer_1":"Piechart"}
    - utter_piechart
* Piechart_code_reco{"answer_1":"Code for Piechart"}
    - utter_ask_code4
* Piechart_seaborn_reco
    - utter_piechart_bokeh   
* thankyou
    - utter_noworries

## Pie chart using Matplotlib

* greet
    - utter_greet
* code_reco
    - utter_ask_code
* data_visualization_reco
    - utter_data_visualization
* Piechart_reco{"answer_1":"Piechart"}
    - utter_piechart
* Piechart_code_reco{"answer_1":"Code for Piechart"}
    - utter_ask_code4
* Piechart_seaborn_reco
    - utter_piechart_matplotlib   
* thankyou
    - utter_noworries

## Pie chart using Plotly

* greet
    - utter_greet
* code_reco
    - utter_ask_code
* data_visualization_reco
    - utter_data_visualization
* Piechart_reco{"answer_1":"Piechart"}
    - utter_piechart
* Piechart_code_reco{"answer_1":"Code for Piechart"}
    - utter_ask_code4
* Piechart_seaborn_reco
    - utter_piechart_plotly  
* thankyou
    - utter_noworries
