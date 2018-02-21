Rails.application.routes.draw do
  # For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html
  
post '/schokotron', to: 'schokotron#create'
get '/schokotron/:provider_id/user', to: 'schokotron#index_user_requests'
get '/schokotron/users', to: 'schokotron#index_all_users'
get '/schokotron/requests', to: 'schokotron#index_all_requests'

end
