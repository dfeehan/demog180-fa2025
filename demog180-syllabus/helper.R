###########################################################
## Some helper functions for the syllabus


library(googlesheets4)
library(googledrive)
library(readxl)
library(writexl)
library(tibble)
library(knitr)
library(kableExtra)
library(dplyr)
# my helper package
library(syllabusr)
library(lubridate)
library(purrr)
library(stringr)
library(glue)
library(gt)

# see
# https://github.com/tidyverse/googlesheets4/issues/274
range_read_cells_format <- function(
    ss, sheet = NULL, range = NULL, skip = 0, n_max = Inf,
    discard_empty = TRUE, group = c('background', 'text', 'other')) {
  
  group = match.arg(group)
  oot <- range_read_cells(ss, sheet, range, skip, n_max, 'full', discard_empty)
  
  if (group == 'background') {
    # for some colors, one or more components may be missing from the list
    out <- list()
    for (p in c('red', 'green', 'blue')) {
      y <- map(
        oot$cell, ~ .x$effectiveFormat$backgroundColorStyle$rgbColor[[p]])
      out[[p]] <- map_dbl(y, ~ if (is.null(.x)) 0 else .x) # RStudio no like
    }
    out <- tibble::as_tibble(out)
    
  } else if (group == 'text') {
    cols <- c(
      'fontFamily', 'fontSize', 'bold', 'italic', 'strikethrough', 'underline')
    out1 <- map_dfr(oot$cell, ~ .x$effectiveFormat$textFormat[cols])
    
    out2 <- list()
    for (p in c('red', 'green', 'blue')) {
      y <- map(
        oot$cell,
        ~ .x$effectiveFormat$textFormat$foregroundColorStyle$rgbColor[[p]])
      out2[[p]] <- map_dbl(y, ~ if (is.null(.x)) 0 else .x) # RStudio no like
    }
    out2 <- tibble::as_tibble(out2)
    out <- cbind(out1, out2)
    
  } else {
    out1 <- map_dfr(oot$cell, ~ .x$effectiveFormat$padding)
    # colnames(out1) = paste0('padding_', colnames(out1))
    
    cols = c('horizontalAlignment', 'verticalAlignment',
             'wrapStrategy', 'hyperlinkDisplayType')
    out2 <- map_dfr(oot$cell, ~ .x$effectiveFormat[cols])
    out <- cbind(out1, out2)
    
  }
  
  out <- oot %>%
    dplyr::select(!cell) %>%
    cbind(out)
  out
}

#d1 <- range_read_cells_format(ss, sheet, range, group = 'background')
#d2 <- range_read_cells_format(ss, sheet, range, group = 'text')
#d3 <- range_read_cells_format(ss, sheet, range, group = 'other')


grab_syllabus_gsheet <- function(class_url, class_fn="demog180") {
  
  googlesheets4::gs4_deauth()
  googledrive::drive_deauth()
  

  
  #content_range <- "C2:I32"
  content_range_row_offset <- 2
  content_range_col_offset <- 3 
  content_range_height <- 31
  content_range_width <- 7
  content_range <- toupper(paste0(letters[content_range_col_offset], 
                                  content_range_row_offset, 
                                  ":", 
                                  letters[content_range_col_offset+content_range_width-1], 
                                  content_range_row_offset + content_range_height - 1))
  
  sheet <- drive_get(class_url) %>%
    read_sheet(sheet='overview', 
               range=content_range)
  
  # read the cell colors
  cell_col <- drive_get(class_url) %>% range_read_cells_format(sheet='overview', 
                                                               range=content_range, 
                                                               group = 'background')
  
  # we'll blank out any cells whose background color is not white
  # (this allows us to easily stage stuff in the google sheet, and then
  #  publish it by changing the background color + recompiling)
  cell_to_blank <- cell_col %>% filter(red < 1 | blue < 1 | green < 1)
  
  # write a local, xlsx version of the syllabus
  write_xlsx(list(overview=sheet),
             path=paste0(class_fn, '.xlsx'))
  
  # and read that local version in, so that we're working with a read_excel object
  tab <- read_excel(paste0(class_fn, '.xlsx'), 
                    sheet='overview')
  
  # now turn cells that have background that is some color other than white into blank 
  # (they are not to be published yet)
  if(nrow(cell_to_blank) > 0) {
    for(i in 1:nrow(cell_to_blank)) {
      cur_row <- cell_to_blank[i,]
      #tab[cur_row$row - content_range_row_offset, cur_row$col - content_range_col_offset + 1] <- "XXX"
      tab[cur_row$row - content_range_row_offset, cur_row$col - content_range_col_offset + 1] <- NA
    }
  }
  
  return(tab)
}