class SchokotronController < ApplicationController
  before_action :set_user, only: [:create, :index_user_requests]

  # POST 
  def create
    unless @user
      @user = User.create!(safe_params)        
    end
    request = @user.requests.create!
    json_response(request, 202)
  end

  # GET 
  def index_all_requests
    requests = Request.all
    json_response(requests)
  end

  # GET 
  def index_all_users
    users = User.all
    json_response(users, 200)
  end

  # GET 
  def index_user_requests
    requests = @user.requests.all
    json_response(requests)
  end


  def safe_params
    params.require(:user).permit(:provider_id, :username, :full_name, :email)
  end

  def set_user
    is_get = params.has_key?(:provider_id)
    provider_id = is_get ? params[:provider_id] : params[:user][:provider_id]
    @user = User.find_by(provider_id: provider_id)
  end

end


