def cigar_party(cigars, is_weekend):
  if is_weekend==True and cigars>=40:
    return True
  elif cigars>=40 and cigars<=60 and is_weekend==False:
    return True
  else:
    return False
