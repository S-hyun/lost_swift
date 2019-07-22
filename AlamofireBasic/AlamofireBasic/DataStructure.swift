//
//  DataStructure.swift
//  AlamofireBasic
//
//  Created by swuad_12 on 11/07/2019.
//  Copyright © 2019 swuad_12. All rights reserved.
//

import Foundation
// {"token":"97241e4770455e35c665e07266b2558dbad0f441"}
struct Token:Codable {
    var token:String
}
struct UserInfo:Codable {
    var id:Int?
    var username:String
    var password:String?
    var email:String
    var message:String
    var profile:URL?
}

struct Product:Codable{
    var id :Int
    var owner:User
    var category:Category
    var comments:[Comment]?
    var title:String
    var slug:String
    var image:URL
    var delivery:Int
    var description:String
    var price:Int
    var active:Bool
    var created:String
    var updated:String
}

struct User:Codable {
    var id:Int
    var username:String
}
struct Category:Codable {
    var id:Int
    var name:String
    var slug:String
}
struct Comment:Codable {
    var id: Int
    var writer: User
    var rate:Int
    var comment:String
    var created:String
    var product:Int
}
