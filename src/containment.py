def check_line_containment(line_1, line_2):
  return (line_1[0] <= line_2[0] and line_1[1] >= line_2[1])


def containment(rec_1, rec_2):
  is__rec_1__in__rec_2 = check_line_containment(rec_1.get('x'), rec_2.get(
      'x')) and check_line_containment(rec_1.get('y'), rec_2.get('y'))
      
  is__rec_2__in__rec_1 = check_line_containment(rec_2.get('x'), rec_1.get(
      'x')) and check_line_containment(rec_2.get('y'), rec_1.get('y'))

  return is__rec_1__in__rec_2 or is__rec_2__in__rec_1
