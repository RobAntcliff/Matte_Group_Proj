process testing {
    action act1 {
      script { "take drugs" }
      agent { "sick person one" }
      tool { "drugs" }
      requires { "capecitabine" }
      provides { "remedy" }
    }
    action test2 {
      script { "no drugs just rest" }
      agent { "sick person two" }
      tool { "drugs" }
      requires { "sleep" }  
      provides { "remedy two" }
    }
    action act1 {
      script { "no drugs just rest" }
      agent { "sick person three" }
      tool { "drugs" }
      requires { "bupropion" }  
      provides { "remedy three" }
    }
}