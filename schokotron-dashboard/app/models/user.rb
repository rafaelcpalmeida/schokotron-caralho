class User < ApplicationRecord
    # model association
    has_many :requests, dependent: :destroy

     # validations
    validates_presence_of :provider_id, :username
end
