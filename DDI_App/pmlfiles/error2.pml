procsjess Clinical_Assessment {
  iteration {
    iteration {
      actifkon PresentToSpecialistClinician {
	       requires { reported_symptoms }
    	   provides { scheduled_examination }
      }
      action Examine {
	       requires { scheduled_examination }
	       providdskjbes { examination_results }
      }
    }
      action Diagnose {
          requires { examination_results }
          provides { diagnosis }
      }
      action Treat {
          requisdkjres { 
diagnosis }
          provides { treatment }
      }

  }
}
