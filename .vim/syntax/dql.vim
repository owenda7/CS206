" Vim syntax file
" Language: DelightQL
" Maintainer: Daniel Eklund
" Latest Revision: 2020-03-24 

if exists("b:current_syntax")
  finish
endif

syn case ignore

" Keywords
syntax keyword  dqlKeywords scalar as  D G O L H assert insert is not like
syntax keyword  dqlBooleans true false null  
syntax keyword  dqlBooleans _ 
syntax match  dqlFunction "\v\zs\w+:(\[?[A-Za-z_,]+\]?)?\ze\(" 
syntax match  dqlFunction "\v\zsf:([A-Za-z_]+)?\ze\"" 
syntax match  dqlStructure "\v\(" 
syntax match  dqlStructure "\v\)" 
syntax match  dqlStructure "\v\{" 
syntax match  dqlStructure "\v\}" 
syntax match  dqlOperator "\v\|\>" 
syntax match  dqlOperator "\v\@" 
syntax match  dqlOperator "\v\#" 
syntax match  dqlOperator "\v\|\=" 
syntax match  dqlOperator "\v\=" 
syntax match  dqlOperator "\v\:\-" 
syntax match  dqlOperator "\v\<\-" 
syntax match  dqlOperator "\v\*" 
syntax match  dqlOperator "\v\." 
syntax match  dqlDelimiter "\v," 
syntax match  dqlDelimiter "\v;" 
syntax match  dqlDelimiter "\v\>" 
syntax match  dqlDelimiter "\v\>;" 
syntax match  dqlDelimiter "\v\>;\<" 
syntax match  dqlDelimiter "\v\>," 
syntax match  dqlDelimiter "\v,\<" 
syntax match  dqlDelimiter "\v\>,\<" 
syntax match  dqlUnaryOp "\v\[" 
syntax match  dqlUnaryOp "\v\+\[" 
syntax match  dqlUnaryOp "\v\]" 
syntax match dqlNumber "\v<\d+>"
syntax match dqlNumber "\v<\d+\.\d+>"
syntax match dqlNumber "\v<\d*\.?\d+([Ee]-?)?\d+>"
syntax match dqlNumber "\v<0x\x+([Pp]-?)?\x+>"
syntax match dqlNumber "\v<0b[01]+>"
syntax match dqlNumber "\v<0o\o+>"

syntax region dqlString start=/"/ skip=/\\"/ end=/"/ oneline contains=dqlInterpolatedWrapper
syntax region dqlInterpolatedWrapper start="\v\\\(\s*" end="\v\s*\)" contained containedin=dqlString contains=dqlInterpolatedString
syntax match dqlInterpolatedString "\v\w+(\(\))?" contained containedin=dqlInterpolatedWrapper

syntax region dqlString start=/`/ skip=/\\`/ end=/`/ oneline contains=dqlInterpolatedWrapper
syntax region dqlInterpolatedWrapper start="\v\\\(\s*" end="\v\s*\)" contained containedin=dqlString contains=dqlInterpolatedString
syntax match dqlInterpolatedString "\v\w+(\(\))?" contained containedin=dqlInterpolatedWrapper

highlight default link dqlKeywords Keyword
highlight default link dqlStructure Structure
highlight default link dqlOperator Type
highlight default link dqlDelimiter Delimiter
highlight default link dqlUnaryOp Type
highlight default link dqlInline Include
highlight default link dqlString String
highlight default link dqlBooleans Boolean
highlight default link dqlNumber Number
highlight default link dqlFunction Number


let b:current_syntax = "dql"
