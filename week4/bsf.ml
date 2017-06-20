(* link.txtから隣接リストを作る *)
(* make_adj_list : (int * 'a) list -> (int * 'a list) list *)
let rec links lst n = match lst with
    [] -> []
  | (page, link) :: rest ->
    if n = page then link :: (links rest n) else links rest n

let rec make_adj_redundant_list lst n = 
    let pair = (n, links lst n) in
    if n < 0 then []
    else pair :: make_adj_redundant_list lst (n-1)
           
let make_adj_list lst =
  let n = match (List.rev lst) with
      [] -> raise Not_found
    | (page, link) :: _ -> page in
  make_adj_redundant_list lst n
  
  
let sample_links =
  [(1, 8); (1, 4); (1, 7);
   (2, 1); (2, 4);
   (3, 9); (3, 6); (3, 5); (3, 4)]

let test1 = links sample_links 1 = [8; 4; 7]
let test2 = links sample_links 0 = []
let test3 = make_adj_redundant_list sample_links (List.length sample_links)
            = [(9, []); (8, []); (7, []); (6, []); (5, []); (4, []);
               (3, [9; 6; 5; 4]);
               (2, [1; 4]);
               (1, [8; 4; 7]);
               (0, [])]
let test4 = make_adj_list sample_links 
            = [(3, [9; 6; 5; 4]); (2, [1; 4]); (1, [8; 4; 7]); (0, [])]


(* 幅優先探索をする *)
