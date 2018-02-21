class CreateUsers < ActiveRecord::Migration[5.1]
  def change
    create_table :users do |t|
      t.string :provider_id
      t.string :username
      t.string :full_name
      t.string :email

      t.timestamps
    end
  end
end
