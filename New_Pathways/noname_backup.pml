process testing {
    action test {
      script { "take drugs" }
      agent { "sick person" }
      tool { "drugs" }
      requires { "capecitabine" }
      provides { "remedy" }
    }
    action {
      script { "no drugs just rest" }
      agent { "sick person" }
      tool { "drugs" }
      requires { "sleep" }  
      provides { "remedy" }
    }
    action test3 {
      script { "no drugs just rest" }
      agent { "sick person" }
      tool { "drugs" }
      requires { "bupropion" }  
      provides { "remedy" }
    }
    action test5 {
      script { "no drugs just rest" }
      delay {"2 weeks"}
      agent { "sick person" }
      tool { "drugs" }
      requires { "bupropion" } 
      frequency {"monthly"} 
      provides { "remedy" }
    }
}